from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db import IntegrityError
import datetime
import operator
import json

from .models import Plan, User, Profile, Fragment

# Create your views here.

#Index page

def index(request):
    #Also check if the user already has profile (if he doesn't then - create one)
    print(request.user)
    try:
        user = User.objects.get(username = request.user)
    except:
        return render(request, "dietApp/index.html")
    try:
        profile = Profile.objects.get(user = user)
        print("profile exist")
        print(profile)
    except:
        profile = Profile(user=user, age=24)
        profile.save()
    print(profile)
    print("index page request")
    return render(request, "dietApp/index.html")


#Log in and register functions
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "dietApp/response.html", {
                "message": "Invalid name and/or password."
            })
    else:
        return render(request, "dietApp/response.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "dietApp/response.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "dietApp/response.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "dietApp/response.html", {
            "message": "Bad request, try one more time",
        })

def profile(request, user):
    print("Profile rendering")
    profile = Profile.objects.get(user = request.user)
    dates = profile.days.all()
    datesList = []
    caloriesList = []
    totalCaloriesList = []
    totalBurntList = []
    burntList = []
    cfpList = []
    totalCalories = 0
    totalBurnt = 0
    weekCounter = 1
    ordered = sorted(dates, key=operator.attrgetter('pk'))
    print(ordered)
    for date in ordered:
        print(totalCaloriesList)
        print("SAS")
        print(date.date.strftime('%B'))
        if date.date.day == datetime.date.today().day:
            cfpList.append(date.carbs)
            cfpList.append(date.fats)
            cfpList.append(date.proteins)
        if date.date.month == datetime.date.today().month:
            totalCalories = totalCalories + date.calories
            totalBurnt = totalBurnt + date.burnt
            print(date.date.weekday())
            if date.date.weekday() == 0:
                print("IT IS MONDAY")
                datesList.append(f"Week {weekCounter}; Day:{date.date.day}")
                totalCaloriesList.append(totalCalories)
                totalBurntList.append(totalBurnt)
                caloriesList.append(date.calories)
                burntList.append(date.burnt)
                totalCalories = 0
                totalBurnt = 0
                weekCounter = weekCounter + 1
                print(totalCaloriesList)
                print(totalBurntList)
            else:
                print("It is not monday")
        else:
            print("Wrong month")
    print(profile.user)
    print(ordered)
    print("*"*85)
    #Checks if the user has a chosen diet plan
    if (profile.plan):
        return render(request, 'dietApp/profile.html', {
        "dates": ordered,
        "datesList": datesList,
        "caloriesList": totalCaloriesList,
        "burntList": totalBurntList,
        "cfpList": cfpList,
        'plan': profile.plan,
    })
    else:
        return render(request, 'dietApp/profile.html', {
            "dates": ordered,
            "datesList": datesList,
            "caloriesList": totalCaloriesList,
            "burntList": totalBurntList,
            "cfpList": cfpList,
        })

def create_day(request):
    if request.method == "POST":
        print("REQUEST")
        profile = Profile.objects.get(user = request.user)
        check = profile.days.filter(date = datetime.datetime.today())
        if check:
            return render(request, "dietApp/response.html", {
                "message": "You have already filled todays form. Wait till the next day"
            })
        else:
            print('date has been added into the database')
        print(profile.user)
        try:
            calorie = int(request.POST.get("calories"))
            burnt = int(request.POST.get('burnt'))
            fats = int(request.POST.get('fats'))
            carbs = int(request.POST.get('carbs'))
            proteins = int(request.POST.get('proteins'))
        except:
            return render(request, 'dietApp/response.html', {
                "message": "Wrong format of the field (Only numbers are acceptable)"
            })
        if int(fats)+int(carbs)+int(proteins) != 100:
            print(int(fats)+int(carbs)+int(proteins))
            return render(request, 'dietApp/response.html', {
                "message": "Wrong format for the fats/carbs/proteins ration ( It shouldn't exceed/belittle a number of 100 )"
            })
        day = Fragment(date = datetime.datetime.today(), calories = calorie, burnt = burnt, fats = fats, carbs = carbs,     proteins = proteins)
        day.save()
        profile.days.add(day)
        print("*********")
        print(day.calories)
        return HttpResponseRedirect(reverse('profile', args=[request.user.username]))
    else:
        return JsonResponse({"message": "Wrong request method"}, status = 404)

@login_required
@csrf_exempt
def render_day(request,day):
    fragment = list(Fragment.objects.filter(pk=day).values())
    print("*"*58)
    print(fragment)
    return JsonResponse(fragment, safe=False, status = 200)

def diet_plans(request):
    return render(request, 'dietApp/plans.html')

@login_required
@csrf_exempt
def add_plan(request):
    profile = Profile.objects.get(user=request.user)
    data = json.loads(request.body)
    plan = data.get("name", "")
    description = data.get("description", "")
    advice = data.get('advice', "")
    print(f"add plan {plan}")
    print(f"also don't forget about {description}")
    yourPlan = Plan(name=plan, description= description, advice = advice)
    yourPlan.save()
    try:
        print(profile.plan.pk)
        currentPlan = Plan.objects.get(pk = profile.plan.pk)
        profile.plan = yourPlan
        profile.save()
        currentPlan.delete()
    except:
        yourPlan.save()
        profile.plan = yourPlan
        profile.save()
    return JsonResponse({"message": f"plan {plan} has been added"}, status = 200)