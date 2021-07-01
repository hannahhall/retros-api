from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    """Student Model
    Extends django user to include cohort
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cohort = models.ForeignKey(
        "Cohort", null=True, on_delete=models.SET_NULL, related_name="students")
    github_url = models.URLField()

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        """Full name of student

        Returns:
            string: Gets the first and last name of the associated user object
        """
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def email(self):
        """Student email

        Returns:
            string: Email of associated user object
        """
        return self.user.email
