from django.db import models
from django import forms
# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
     return self.title
