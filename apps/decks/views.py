from rest_framework import viewsets
from rest_framework.response import Response

from apps.cards.apis.serializers import CardsSerializer
from apps.decks.apis.serializers import DecksSerializer
from apps.decks.models import Deck
from apps.cards.models import Card


class DecksViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Deck.objects.all()
    serializer_class = DecksSerializer


class CardsNestedViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk):
        cards = Card.objects.filter(id=decks_pk)
        serializer = CardsSerializer(cards, many=True)
        return Response(serializer.data)
