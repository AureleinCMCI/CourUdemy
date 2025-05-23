from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=200)
    prenom  = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.nom