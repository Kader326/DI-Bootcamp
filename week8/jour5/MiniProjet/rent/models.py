from django.db import models


class Address(models.Model):
    adresse = models.CharField(max_length=200)
    adresse2 = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=200)


class Client(models.Model):
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.EmailField()
    address= models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)

    
    
    def __str__(self):
        return self.nom
    
class Type(models.Model):
    libelle = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.libelle
    
class Taille(models.Model):
    libelle = models.CharField(max_length=200)
    
    def __str__(self):
        return self.libelle
    
    
class Vehicule(models.Model):
    type = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)
    date_creation =models.DateField(auto_now_add=True)
    cout = models.FloatField()
    taille = models.ForeignKey(Taille, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class Location(models.Model):
    date_locat = models.DateField()
    date_retour = models.DateField()
    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.date_locat
    
class Tarif(models.Model):
    taux = models.FloatField()
    type_v =  models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)
    taille_v = models.ForeignKey(Taille, null=True, blank=True, on_delete=models.CASCADE)
    

class RentalStation(models.Model):
    nom = models.CharField(max_length=200)
    capacité = models.IntegerField()
    address= models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)


# Create your models here.
