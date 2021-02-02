from datetime import date

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


# /decks/:id/cards -> the id will be assigned in decks_pk
class CardsNestedViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk):
        queryset = Card.objects.filter(deck=decks_pk)
        serializer = CardsSerializer(queryset, many=True)
        return Response(serializer.data)


class TodaysCardsViewSet(viewsets.ViewSet):
    def list(self, request, decks_pk):
        today = date.today()
        queryset = Card.objects.filter(deck=decks_pk,
                                       next_review_at__day=today.day)

        serializer = CardsSerializer(queryset, many=True)
        return Response(serializer.data)
