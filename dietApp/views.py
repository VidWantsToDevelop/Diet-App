from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db import IntegrityError

from .models import User, Profile, Fragment

# Create your views here.

#Index page

def index(request):
    #Also check if the user already has profile (if he doesn't then - create one)
    print(request.user)
    user = User.objects.get(username = request.user)
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
    return render(request, 'dietApp/profile.html')

def create_day(request):
    print("REQUEST")
    profile = Profile.objects.get(user = request.user)
    print(profile.user)
    calorie = 3650
    burnt = 1532
    fats = 25
    carbs = 40
    proteins = 35
    day = Fragment(calories = calorie, burnt = burnt, fats = fats, carbs = carbs, proteins = proteins)
    day.save()
    print(day.calories)
    print("*********")
    print(Fragment.objects.filter(calories = 2230))
    return render(request, 'dietApp/index.html')