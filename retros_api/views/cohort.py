from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from retros_api.models import Cohort
from retros_api.serializers import CohortDefaultSerializer, CohortDetailSerializer
from .base import MultiSerializerViewSet


class CohortViewSet(MultiSerializerViewSet):
    """View for Cohort Model
    GET, POST, RETRIEVE, DELETE
    my_cohorts - logged in instructor's cohorts
    """
    serializers = {
        'default': CohortDefaultSerializer,
        'retrieve': CohortDetailSerializer
    }

    permission_classes = [IsAdminUser]
    queryset = Cohort.objects.all()

    @action(methods=["GET"], detail=False)
    def my_cohorts(self, request):
        """Get the instructor's cohorts
        """
        serializer = CohortDefaultSerializer(request.user.cohorts, many=True)
        return Response(serializer.data)
