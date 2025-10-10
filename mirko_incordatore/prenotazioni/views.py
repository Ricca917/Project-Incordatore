from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import PuntoRitiro, Servizio, Prenotazione
from .forms import PrenotazioneForm

# Visualizza tutti i punti di ritiro
def punti_ritiro_view(request):
    punti = PuntoRitiro.objects.all()
    return render(request, "core/punti_ritiro.html", {"punti": punti})

# Visualizza tutti i servizi disponibili
def servizi_view(request):
    servizi = Servizio.objects.all()
    return render(request, "core/servizi.html", {"servizi": servizi})

# Visualizza tutte le prenotazioni dell'utente loggato
@login_required
def prenotazioni_utente_view(request):
    prenotazioni = Prenotazione.objects.filter(cliente=request.user)
    return render(request, "core/prenotazioni_utente.html", {"prenotazioni": prenotazioni})

# Crea una nuova prenotazione via form HTML
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
            messages.success(request, "Prenotazione creata con successo!")
            return redirect("prenotazioni-utente")
        else:
            messages.error(request, "Errore nella creazione della prenotazione. Controlla i dati inseriti.")
    else:
        form = PrenotazioneForm()

    return render(request, "core/crea_prenotazione.html", {"form": form, "punti": punti, "servizi": servizi})
