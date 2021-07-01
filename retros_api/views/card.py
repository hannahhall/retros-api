from rest_framework import viewsets, mixins
from retros_api.serializers import CardDefaultSerializer
from retros_api.permissions import IsOwnerOrAdmin
from retros_api.models import Card


class CardViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    POST, PUT, DELETE viewset for Card model
    Must be owner or admin to access
    """
    serializer_class = CardDefaultSerializer
    queryset = Card.objects.all()
    permission_classes = [IsOwnerOrAdmin]
