from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer): 
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data): # Metodo per creare un nuovo utente con password hash sicuro
        user = User(
            username=validated_data["username"],
            email=validated_data.get("email", "")
        )
        user.set_password(validated_data["password"])  # password hash sicuro
        user.save()
        return user


    def update(self, instance, validated_data): # Metodo per aggiornare i dati dell'utente
        for attr, value in validated_data.items():
            if attr == "password": # Se si aggiorna la password
                instance.set_password(value) # Aggiorna la password con hash sicuro
            else:
                setattr(instance, attr, value) # Aggiorna gli altri campi
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email","password")


    def update(self, instance, validated_data): # Metodo per aggiornare il profilo utente
        instance.username = validated_data.get("username", instance.username) # Aggiorna il nome utente
        instance.email = validated_data.get("email", instance.email) # Aggiorna l'email
        
        password = validated_data.get("password", None) # Ottiene la nuova password se fornita
        if password:
            instance.set_password(password) # Aggiorna la password con hash sicuro
        instance.save()
        return instance
    