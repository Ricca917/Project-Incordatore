from django.contrib import admin
from .models import PuntoRitiro, Servizio, Prenotazione

# Register your models here.


admin.site.register(PuntoRitiro)
admin.site.register(Servizio)
admin.site.register(Prenotazione)