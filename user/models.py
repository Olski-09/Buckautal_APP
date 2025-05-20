from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField("Vorname", max_length=200)
    last_name = models.CharField("Name", max_length=200)
    email = models.EmailField("Email-Adresse", max_length=200)
    username = models.CharField("Nutzername", max_length=200)