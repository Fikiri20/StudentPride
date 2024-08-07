from django.shortcuts import render
from .models import Faith

# Create your views here.
def faith(request):
    faiths = Faith.objects.all()
    context = {'faiths': faiths}
    return render(request, 'faith/faith.html', context)