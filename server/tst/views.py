from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer

# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer