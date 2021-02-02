from django.urls import path, include
from rest_framework_nested import routers
from .views import DecksViewSet, CardsNestedViewSet


# decks  -> /decks/
# deck  -> /decks/:id
# nested cards in deck  -> /decks/:id/cards

router = routers.SimpleRouter()
router.register('', DecksViewSet)

cards_router = routers.NestedSimpleRouter(router, r'', lookup='decks')
cards_router.register(r'cards', CardsNestedViewSet, basename='deck_cards')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls))
]
