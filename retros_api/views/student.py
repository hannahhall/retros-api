from rest_framework import mixins
from rest_framework import viewsets
from retros_api.serializers import StudentDetailSerializer
from retros_api.permissions import IsOwnerOrAdmin
from retros_api.models import Student

class StudentViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A retrive ViewSet for viewing a single student.
    """
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()
    permission_classes = [IsOwnerOrAdmin]
