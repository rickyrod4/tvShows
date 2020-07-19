from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    