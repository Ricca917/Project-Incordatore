from rest_framework import serializers
from .models import Prenotazione, Servizio, PuntoRitiro


class PuntoRitiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoRitiro
        fields = "__all__"


class ServizioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servizio
        fields = "__all__"


class PrenotazioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prenotazione
        fields = [
            "id",
            "cliente",
            "nome_cliente",
            "telefono",
            "servizio",
            "punto_ritiro",
            "data_preferita",
            "ora_preferita",
            "marca_racchetta",
            "note",
            "stato",
            "creato_il",
            "aggiornato_il",
        ]
        read_only_fields = ["cliente", "creato_il", "aggiornato_il"]