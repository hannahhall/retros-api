from django.db import models
from django.contrib.auth.models import User


class Cohort(models.Model):
    """Cohort Model
    """
    instructors = models.ManyToManyField(
        User, related_name="cohorts")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
