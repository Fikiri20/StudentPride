from django.shortcuts import render
from .models import Club

def club(request):
    clubs = Club.objects.all()
    context = {'clubs': clubs}
    return render(request, 'club/clubs.html', context)
