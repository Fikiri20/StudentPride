from django.shortcuts import render
from .models import Association

def association(request):
    associates = Association.objects.all()
    context = {'associates': associates}
    return render(request, 'association/association.html', context)
