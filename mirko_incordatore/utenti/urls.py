from django.urls import path
from .views import register_html_view, login_html_view, logout_html_view

urlpatterns = [
    path("register/", register_html_view, name="register-html"),
    path("login/", login_html_view, name="login-html"),
    path("logout/", logout_html_view, name="logout-html"),
]
