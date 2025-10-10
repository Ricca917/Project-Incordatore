from django.urls import path
from .views import register_html_view, login_html_view, logout_html_view, user_profile_view

urlpatterns = [
    path("register/", register_html_view, name="register-html"), # rotta per la registrazione
    path("login/", login_html_view, name="login-html"), # rotta per il login
    path("logout/", logout_html_view, name="logout-html"), # rotta per il logout
    path("profilo/", user_profile_view, name="user-profile"),  # nuova rotta per il profilo utente    
]
