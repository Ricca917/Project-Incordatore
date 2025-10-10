from django.db import models
from django.conf import settings
from django.utils import timezone

class PuntoRitiro(models.Model): # modello per i punti di ritiro
    nome = models.CharField(max_length=100)
    indirizzo = models.CharField(max_length=255, blank=True)
    note = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Punto di Ritiro"
        verbose_name_plural = "Punti di Ritiro"

    def __str__(self):
        return self.nome


class Servizio(models.Model): # modello per i servizi offerti
    nome = models.CharField(max_length=100)    
    descrizione = models.TextField(blank=True) 
    prezzo = models.DecimalField(max_digits=7, decimal_places=2)
    
    class Meta:
        verbose_name = "Servizio"
        verbose_name_plural = "Servizi"

    def __str__(self):
        return f"{self.nome} - €{self.prezzo}"


class Prenotazione(models.Model): # modello per le prenotazioni
    STATI = [
        ("in_attesa", "In attesa"),
        ("confermata", "Confermata"),
        ("completata", "Completata"),
        ("annullata", "Annullata"),
    ]

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )
    nome_cliente = models.CharField(max_length=120)
    telefono = models.CharField(max_length=30, blank=True)
    servizio = models.ForeignKey(Servizio, on_delete=models.PROTECT)
    punto_ritiro = models.ForeignKey(PuntoRitiro, on_delete=models.PROTECT)
    data_preferita = models.DateField()
    ora_preferita = models.TimeField()
    marca_racchetta = models.CharField(max_length=100, blank=True)
    note = models.TextField(blank=True)
    stato = models.CharField(max_length=20, choices=STATI, default="in_attesa")
    creato_il = models.DateTimeField(default=timezone.now)
    aggiornato_il = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Prenotazione"
        verbose_name_plural = "Prenotazioni"

    def __str__(self):
        return f"{self.nome_cliente} - {self.servizio} ({self.data_preferita})"
