from django.shortcuts import render
from .models import Networking, Items

def networking(request):
    networks = Networking.objects.all()
    items = Items.objects.all()
    context = {'networks': networks, 'items': items}
    return render(request, 'networking/networking.html', context)