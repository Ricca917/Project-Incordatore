from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from prenotazioni.models import PuntoRitiro
from prenotazioni.models import Servizio
from prenotazioni.models import Prenotazione



# Create your views here.


def index(request):
    return render(request, "core/index.html")


def punti_ritiro_view(request):
    punti = PuntoRitiro.objects.all()
    return render(request, "core/punti_ritiro.html", {"punti": punti})


def servizi_view(request):
    servizi = Servizio.objects.all()
    return render(request, "core/servizi.html", {"servizi": servizi})


@login_required
def profilo_view(request):
    user = request.user
    return render(request, "core/profilo.html", {"user": user})


@login_required
def prenotazioni_utente_view(request):
    prenotazioni = Prenotazione.objects.filter(cliente=request.user)
    return render(request, "core/prenotazioni_utente.html", {"prenotazioni": prenotazioni})


@login_required
def crea_prenotazione_view(request):
    punti = PuntoRitiro.objects.all()
    servizi = Servizio.objects.all()

    if request.method == "POST":
        punto_id = request.POST.get("punto_ritiro")
        servizio_id = request.POST.get("servizio")
        data_ora = request.POST.get("data_ora")

        Prenotazione.objects.create(
            cliente=request.user,
            punto_ritiro_id=punto_id,
            servizio_id=servizio_id,
            data_ora=data_ora
        )
        return redirect("prenotazioni-utente")

    return render(request, "core/crea_prenotazione.html", {"punti": punti, "servizi": servizi})