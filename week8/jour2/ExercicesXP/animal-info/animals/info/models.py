from lib2to3.pygram import pattern_symbols
from django.db import models

class Animal(models.Model):
    pattes= models.fields.IntegerField()
    poids= models.fields.IntegerField()
    taille= models.fields.IntegerField()
    vitesse= models.fields.IntegerField()
    famille=models.fields.CharField(max_length=30)

class Famille(models.Model):
    nom=models.fields.CharField(max_length=40)

# Create your models here.
