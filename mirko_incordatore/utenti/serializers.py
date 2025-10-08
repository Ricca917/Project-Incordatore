from django.contrib.auth import get_user_model # importa il modello utente attivo nel progetto Django
from rest_framework import serializers 

User = get_user_model() # User prende il modello utente attivo nel progetto Django

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "password") # campi esposti per modello User
        
        
    def create(self, validated_data):   # funzione per creare un nuovo utente, chiede username, email e passwword per la registrazione
        user = User(
            username =validated_data["username"],
            email=validated_data("email","")
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
        