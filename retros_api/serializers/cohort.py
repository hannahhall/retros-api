from rest_framework.serializers import ModelSerializer
from retros_api.models import Cohort
from .student import StudentDetailSerializer


class CohortDefaultSerializer(ModelSerializer):
    """Default serializer for Cohort Model
    """
    class Meta:
        model = Cohort
        fields = '__all__'


class CohortDetailSerializer(ModelSerializer):
    """Detail Serializer for Cohort, includes list of students
    """
    students = StudentDetailSerializer(many=True)

    class Meta:
        model = Cohort
        fields = ['id', 'students', 'name']
