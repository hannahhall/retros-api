from django.db import models


class Retro(models.Model):
    """Retro Model

    """
    student = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="retros")
    start_date = models.DateField()
    end_date = models.DateField()
