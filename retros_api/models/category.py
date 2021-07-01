from django.db import models


class Category(models.Model):
    """Category Model
    """
    label = models.CharField(max_length=15)

    def __str__(self):
        return self.label  
