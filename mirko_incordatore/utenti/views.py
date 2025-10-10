from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def register_html_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrazione avvenuta con successo!")
            return redirect("home")
        else:
            messages.error(request, "Correggi gli errori nel modulo.")
    else:
        form = UserCreationForm()
    return render(request, "core/register.html", {"form": form})

def login_html_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Benvenuto {user.username}!")
            return redirect("home")
        else:
            messages.error(request, "Username o password non corretti.")
    else:
        form = AuthenticationForm()
    return render(request, "core/login.html", {"form": form})

def logout_html_view(request):
    logout(request)
    messages.info(request, "Logout effettuato correttamente.")
    return redirect("home")
