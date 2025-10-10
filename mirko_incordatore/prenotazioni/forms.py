from django import forms
from django.utils import timezone
from .models import Prenotazione

class PrenotazioneForm(forms.ModelForm): # Form per creare una prenotazione
    class Meta:
        model = Prenotazione
        fields = [
            "nome_cliente",
            "telefono",
            "servizio",
            "punto_ritiro",
            "data_preferita",
            "ora_preferita",
            "marca_racchetta",
            "note",
        ]
        widgets = {
            "data_preferita": forms.DateInput(attrs={"type": "date"}),
            "ora_preferita": forms.TimeInput(attrs={"type": "time"}),
        }

    def clean_data_preferita(self): # Controlla che la data non sia nel passato
        data = self.cleaned_data["data_preferita"]
        if data < timezone.localdate():
            raise forms.ValidationError("La data non può essere nel passato.")
        return data

    def clean_ora_preferita(self): # Controlla che l'ora sia tra le 09:00 e le 19:00
        ora = self.cleaned_data["ora_preferita"]
        if ora.hour < 9 or ora.hour > 19:
            raise forms.ValidationError("L'orario deve essere tra le 09:00 e le 19:00.")
        return ora

    def clean(self): # Controlla che non ci siano prenotazioni duplicate per lo stesso punto di ritiro, data e ora
        cleaned_data = super().clean()
        data = cleaned_data.get("data_preferita")
        ora = cleaned_data.get("ora_preferita")
        punto = cleaned_data.get("punto_ritiro")

        if data and ora and punto:
            # Controlla se già esiste una prenotazione per quella combinazione
            if Prenotazione.objects.filter(
                data_preferita=data,
                ora_preferita=ora,
                punto_ritiro=punto
            ).exists():
                raise forms.ValidationError(
                    "Questo orario per il punto di ritiro selezionato è già prenotato."
                )

        return cleaned_data
