from django.urls import path
from core.views import punti_ritiro_view, servizi_view, prenotazioni_utente_view, crea_prenotazione_view

urlpatterns = [
    path("punti-ritiro/", punti_ritiro_view, name="punti-ritiro"),
    path("servizi/", servizi_view, name="servizi"),
    path("prenotazioni/", prenotazioni_utente_view, name="prenotazioni-utente"),
    path("prenotazioni/crea/", crea_prenotazione_view, name="crea-prenotazione"),
]
