from django.shortcuts import render, redirect
from .forms import LocationForm, VehiculeForm, ClientForm, RentalStationForm
from django.contrib import  messages


def home(request):
    return render(request, 'rent/home.html')


def rental(request):
    context ={}
    return render(request, 'rent/rental.html', context)


def rental_detail(request, id):
    context ={}
    return render(request, 'rent/rental_detail.html', context)




def add_rent(request):
    if request.method=="POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Location effectué")
            return redirect('type')
        else:
            return render(request, 'rent/add.html', {"form":form})
    else:
        form = LocationForm()
        return render(request, 'rent/add.html', {"form":form})
    
    
def customer(request):
    context ={}
    return render(request, 'rent/customer.html', context)


def customer_detail(request, id):
    context ={}
    return render(request, 'rent/customer_detail.html', context)

  
def add_cust(request):
    if request.method=="POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Location effectué")
            return redirect('customer')
        else:
            return render(request, 'rent/add_cust.html', {"form":form})
    else:
        form = ClientForm()
        return render(request, 'rent/add_cust.html', {"form":form})
    


def vehicle(request):
    context ={}
    return render(request, 'rent/vehicle.html', context)


def vehicle_detail(request, id):
    context ={}
    return render(request, 'rent/vehicle_detail.html', context)


def add_vehi(request):
    if request.method=="POST":
        form = VehiculeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "vehicule effectué")
            return redirect('vehicle')
        else:
            return render(request, 'rent/add_vehi.html', {"form":form})
    else:
        form = VehiculeForm()
        return render(request, 'rent/add_vehi.html', {"form":form})
    



def station(request):
    context ={}
    return render(request, 'rent/station.html', context)


def station_detail(request, id):
    context ={}
    return render(request, 'rent/station_detail.html', context)


def add_station(request):
    if request.method=="POST":
        form = RentalStationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Station effectué")
            return redirect('station')
        else:
            return render(request, 'rent/add_station.html', {"form":form})
    else:
        form = RentalStationForm()
        return render(request, 'rent/add_station.html', {"form":form})
    
    
def distribute(request):
    context ={}
    return render(request, 'rent/distribute.html', context)



def distribution(request):
    context ={}
    return render(request, 'rent/distribution.html', context)
    
# Create your views here.
