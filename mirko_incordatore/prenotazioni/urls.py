from django.urls import path
from .views import PuntoRitiroList, ServizioList, PrenotazioneCreate, PrenotazioneListUser

urlpatterns = [
    path("punti-ritiro/", PuntoRitiroList.as_view(), name="punti-ritiro"),
    path("servizi/", ServizioList.as_view(), name="servizi"),
    path("prenotazioni/", PrenotazioneCreate.as_view(), name="prenotazioni-create"),
    path("prenotazioni/mie/", PrenotazioneListUser.as_view(), name="prenotazioni-mie"),
]