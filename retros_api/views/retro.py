from retros_api.serializers import RetroDetailSerializer, RetroDefaultSerializer
from retros_api.permissions import IsOwnerOrAdmin
from retros_api.models import Retro, Student
from .base import MultiSerializerViewSet


class RetroViewSet(MultiSerializerViewSet):
    """
    GET, POST, PUT, DELETE viewset for Retro model
    Must be owner or admin to access
    """
    serializers = {
        'default': RetroDefaultSerializer,
        'retrieve': RetroDetailSerializer
    }
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        filter_by = self.request.user
        query = self.request.query_params.get('student_id')
        if query is not None and self.request.user.is_staff:
            filter_by = Student.objects.get(pk=query).user
        return Retro.objects.filter(student__user=filter_by)
