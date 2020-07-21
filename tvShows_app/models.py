from django.db import models

class ShowManager(models.Manager):
    def validate(self, form_data):
        errors = {}
        if len(form_data['title']) < 2:
            errors['title'] = "Title must be at least 2 character!"
        if len(form_data['network']) < 2:
            errors['network'] = 'Network must be at least 2 characters'
        if len(form_data['description']) < 10:
            errors['description'] = 'Description must be at least 10 chracters' 
        return errors


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releaseDate = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()