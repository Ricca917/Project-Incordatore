from django.shortcuts import render # importa il metodo render per le viste basate su funzioni
from rest_framework import generics # importa le viste generiche di DRF
from .serializers import UserSerializer 
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class RegisterView(generics.CreateAPIView): # vista per la registrazione di un nuovo utente
    queryset = User.objects.all()   # permette di vedere tutti gli utenti
    serializer_class = UserSerializer 
