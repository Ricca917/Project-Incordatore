from django.urls import path
from .views import RegisterView, UserListView, UserDetailView, UserProfileView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),  # registrazione
    path("", UserListView.as_view(), name="user-list"),          # lista utenti
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),  # dettaglio per ID
    path("profilo/", UserProfileView.as_view(), name="user-profile"), # profilo utente loggato
]
