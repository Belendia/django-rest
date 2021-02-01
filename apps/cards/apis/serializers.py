from rest_framework import serializers

from apps.cards.models import Card
from apps.decks.models import Deck


class CardsSerializer(serializers.ModelSerializer):
    deck = serializers.PrimaryKeyRelatedField(queryset=Deck.objects.all())

    class Meta:
        model = Card
        fields = ('id', 'question', 'answer', 'deck')
