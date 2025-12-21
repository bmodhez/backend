from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid email or password")

    return render(request, "auth/login.html")



def logout_view(request):
    logout(request)
    return redirect("login")
