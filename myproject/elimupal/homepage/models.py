# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add other fields as required

    def __str__(self):
        return self.name
