from rest_framework.serializers import ModelSerializer
from retros_api.models import Student


class StudentDefaultSerializer(ModelSerializer):
    """Default Serializer for Student Model
    """
    class Meta:
        model = Student
        fields = '__all__'


class StudentDetailSerializer(ModelSerializer):
    """Detail Serializer for Student Model
    """
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'github_url', 'retros', 'cohort']


class StudentRetroSerializer(ModelSerializer):
    """Student Serializer for Retro Detail
    """
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'github_url', 'cohort']
        depth = 1
