from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from prenotazioni.models import PuntoRitiro, Servizio, Prenotazione
from prenotazioni.forms import PrenotazioneForm

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
        form = PrenotazioneForm(request.POST)
        if form.is_valid():
            prenotazione = form.save(commit=False)
            prenotazione.cliente = request.user
            prenotazione.nome_cliente = request.user.username
            prenotazione.save()
            messages.success(request, "Prenotazione effettuata con successo!")
            return redirect("prenotazioni-utente")
    else:
        form = PrenotazioneForm()

    return render(request, "core/crea_prenotazione.html", {"form": form, "punti": punti, "servizi": servizi})
