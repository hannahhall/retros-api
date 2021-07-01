from rest_framework import serializers
from retros_api.models import Card


class CardDefaultSerializer(serializers.ModelSerializer):
    """Default Card Serializer
    """
    class Meta:
        model = Card
        fields = '__all__'


class CardDetailSerializer(serializers.ModelSerializer):
    """Detail Card Serializer
    """
    class Meta:
        model = Card
        fields = ['id', 'text', 'category']
        depth = 1
