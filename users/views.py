from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        authenticated_user = authenticate(request, username=username, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "users/login.html")


def register_user(request):
    registration_form = UserCreationForm()

    if request.method == "POST":
        registration_form = UserCreationForm(request.POST)
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            new_user.username = new_user.username.lower()
            new_user.save()
            login(request, new_user)
            return redirect("home")
        else:
            messages.error(request, "An error occurred during Registration")

    context = {"form": registration_form}

    return render(request, "users/register.html", context)


@login_required(login_url="home")
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")
