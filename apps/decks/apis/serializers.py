from rest_framework import serializers

from apps.decks.models import Deck


class DecksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'title', 'description')
