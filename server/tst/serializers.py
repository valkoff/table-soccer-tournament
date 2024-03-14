from rest_framework import serializers
from .models import Player, Team, Match

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'  # Sostituisci con i campi specifici che vuoi includere se necessario

# Ripeti il processo per gli altri modelli
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
