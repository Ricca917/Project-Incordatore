from django.shortcuts import render # importa il metodo render per le viste basate su funzioni
from rest_framework import generics 
from django.contrib.auth import get_user_model # importa il modello utente attivo nel progetto Django
from .serializers import UserSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView): # Endpoint per la registrazione degli utenti
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView): # Endpoint per la lista degli utenti
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView): # Endpoint per i dettagli, aggiornamento e cancellazione di un utente specifico
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileView(generics.RetrieveUpdateAPIView): # Endpoint per visualizzare e aggiornare il profilo dell'utente autenticato
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user