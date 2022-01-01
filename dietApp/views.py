from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db import IntegrityError
import datetime

from .models import User, Profile, Fragment

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
    burntList = []
    cfpList = []
    for date in dates:
        if date.date.day == datetime.date.today().day:
            cfpList.append(date.carbs)
            cfpList.append(date.fats)
            cfpList.append(date.proteins)
        if date.date.month == datetime.datetime.today().month:
            datesList.append(f"Day:{date.date.day} Month:{date.date.month}")
            caloriesList.append(date.calories)
            burntList.append(date.burnt)
        else:
            print("Wrong month")
    print(profile.user)
    print(dates)
    print("*"*85)
    return render(request, 'dietApp/profile.html', {
        "dates": dates,
        "datesList": datesList,
        "caloriesList": caloriesList,
        "burntList": burntList,
        "cfpList": cfpList,
    })

def create_day(request):
    print("REQUEST")
    profile = Profile.objects.get(user = request.user)
    print(profile.user)
    calorie = 1560
    burnt = 1532
    fats = 25
    carbs = 40
    proteins = 35
    day = Fragment(date = datetime.datetime.today(), calories = calorie, burnt = burnt, fats = fats, carbs = carbs, proteins = proteins)
    day.save()
    profile.days.add(day)
    print("*********")
    print(day.calories)
    return JsonResponse({"message": "Data will be updated on your next visit"}, status = 200)

@login_required
@csrf_exempt
def render_day(request,day):
    fragment = list(Fragment.objects.filter(pk=day).values())
    print("*"*58)
    print(fragment)
    return JsonResponse(fragment, safe=False, status = 200)