from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Registrazione via HTML
def register_html_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrazione avvenuta con successo!")
            return redirect("home")
        else:
            messages.error(request, "Correggi gli errori nel modulo.")
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})

# Login via HTML
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

# Logout via HTML
def logout_html_view(request):
    logout(request)
    messages.info(request, "Logout effettuato correttamente.")
    return redirect("home")

# Modifica profilo utente
@login_required
def user_profile_view(request):
    user = request.user
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        if username and email:
            user.username = username
            user.email = email
            user.save()
            messages.success(request, "Profilo aggiornato con successo!")
            return redirect("user-profile")
        else:
            messages.error(request, "Compila tutti i campi correttamente.")
    
    return render(request, "core/user_profile.html", {"user": user})

# Modifica profilo utente con gestione errori
@login_required
def user_profile_view(request):    
    user = request.user

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        if not username or not email:
            messages.error(request, "Compila tutti i campi.")
        else:
            user.username = username
            user.email = email
            try:
                user.save()
                messages.success(request, "Profilo aggiornato con successo!")
            except Exception as e:
                messages.error(request, f"Errore nell'aggiornamento: {str(e)}")

        return redirect("user-profile")

    return render(request, "core/user_profile.html", {"user": user})