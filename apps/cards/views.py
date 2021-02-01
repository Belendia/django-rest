from rest_framework import viewsets

from apps.cards.apis.serializers import CardsSerializer
from apps.cards.models import Card


class CardsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Card.objects.all()
    serializer_class = CardsSerializer
