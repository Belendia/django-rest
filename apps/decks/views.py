from rest_framework import viewsets

from apps.decks.apis.serializers import DecksSerializer
from apps.decks.models import Deck


class DecksViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Deck.objects.all()
    serializer_class = DecksSerializer
