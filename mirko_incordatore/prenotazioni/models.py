from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class PuntoRitiro(models.Model):
    nome = models.CharField(max_length=100)
    indirizzo = models.CharField(max_length=255)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.nome
    

class Servizio(models.Model):
    nome = models.CharField(max_length=100)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)


