from django.db import models

# Create your models here.
class Post(models.Model):
    announcement = models.CharField(max_length=200)
    date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)