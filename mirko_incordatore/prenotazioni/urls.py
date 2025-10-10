from django.urls import path
from .views import PuntoRitiroList, ServizioList, PrenotazioneCreate, PrenotazioneListUser, PrenotazioneList

urlpatterns = [
    
    path("punti-ritiro/", PuntoRitiroList.as_view(), name="punti-ritiro"), 
    path("servizi/", ServizioList.as_view(), name="servizi"),
    path("prenotazioni/create/", PrenotazioneCreate.as_view(), name="prenotazioni-create"),
    path("prenotazioni/user/", PrenotazioneListUser.as_view(), name="prenotazioni-user"),
    path("prenotazioni/view/", PrenotazioneList.as_view(), name="prenotazioni-view"),
    
]