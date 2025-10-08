from django.shortcuts import render 
from rest_framework import generics, permissions  
from .models import PuntoRitiro, Servizio, Prenotazione
from .serializers import PuntoRitiroSerializer, ServizioSerializer, PrenotazioneSerializer 

# Create your views here.


class PuntoRitiroList(generics.ListCreateAPIView): # endpoint relativo ai punti di ritiro
    queryset = PuntoRitiro.objects.all()
    serializer_class = PuntoRitiroSerializer


class ServizioList(generics.ListCreateAPIView): # endpoint relativo ai servizi
    queryset = Servizio.objects.all()
    serializer_class = ServizioSerializer


class PrenotazioneCreate(generics.CreateAPIView): # endpoint per creare una prenotazione
    queryset = Prenotazione.objects.all()
    serializer_class = PrenotazioneSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(cliente=self.request.user)


class PrenotazioneList(generics.ListCreateAPIView): # endpoint per visualizzare tutte le prenotazioni (admin)
    queryset = Prenotazione.objects.all()
    serualizer_class = PrenotazioneSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(cliente=self.request.user)


class PrenotazioneListUser(generics.ListAPIView): # endpoint per visualizzare le prenotazioni dell'utente autenticato
    serializer_class = PrenotazioneSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Prenotazione.objects.filter(cliente= self.request.user)
    