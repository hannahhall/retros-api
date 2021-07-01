from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    """Card Model
    """
    retro = models.ForeignKey(
        "Retro", on_delete=models.CASCADE, related_name="cards")
    category = models.ForeignKey(
        "Category", null=True, on_delete=models.SET_NULL)
    text = models.TextField()
