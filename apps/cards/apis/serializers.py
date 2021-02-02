from rest_framework import serializers

from apps.cards.models import Card
from apps.decks.models import Deck


class CardsSerializer(serializers.ModelSerializer):
    deck = serializers.PrimaryKeyRelatedField(queryset=Deck.objects.all())
    bucket = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Card
        fields = ('id', 'question', 'answer', 'deck', 'bucket',
                  'created_at', 'updated_at')
