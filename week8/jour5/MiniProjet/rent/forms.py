from django import forms
from rent.models import Type, Vehicule, Tarif, Location, Taille, Client, RentalStation, Address



class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        
        
        
class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = '__all__'
        
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
        
class RentalStationForm(forms.ModelForm):
    class Meta:
        model = RentalStation
        fields = '__all__'