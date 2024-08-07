from django.shortcuts import render
from .models import House
# Create your views here.

def housing(request):
    house = House.objects.all()
    context = {'house': house}
    return render(request, 'housing/housing.html', context)


def house(request, pk):
    houseObj = House.objects.get(id=pk)
    houseDetails = houseObj.houseDetails.all()
    context = {'house': houseObj, 'houseDetails': houseDetails}
    return render(request, 'housing/house.html', context)

