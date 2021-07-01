from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    """Student Model
    Extends django user to include cohort
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cohort = models.ForeignKey("Cohort", null=True, on_delete=models.SET_NULL)
