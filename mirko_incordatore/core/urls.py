# core/urls.py
from django.urls import path
from .views import index, punti_ritiro_view, servizi_view, profilo_view, prenotazioni_utente_view, crea_prenotazione_view

urlpatterns = [
    path("", index, name="home"),
    path("punti-ritiro/", punti_ritiro_view, name="punti-ritiro"),
    path("servizi/", servizi_view, name="servizi"),
    path("profilo/", profilo_view, name="profilo"),
    path("prenotazioni/", prenotazioni_utente_view, name="prenotazioni-utente"),
    path("prenotazioni/crea/", crea_prenotazione_view, name="crea-prenotazione"),
]
