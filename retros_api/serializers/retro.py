from rest_framework.serializers import ModelSerializer
from retros_api.models import Retro
from .card import CardDetailSerializer
from .student import StudentRetroSerializer


class RetroDefaultSerializer(ModelSerializer):
    """Default serializer for Retro Model
    """
    class Meta:
        model = Retro
        fields = '__all__'


class RetroDetailSerializer(ModelSerializer):
    """Detail Serializer for Retro Model
    """
    cards = CardDetailSerializer(many=True)
    student = StudentRetroSerializer()

    class Meta:
        model = Retro
        fields = ['id', 'student', 'cards']
