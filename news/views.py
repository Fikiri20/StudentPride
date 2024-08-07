from django.shortcuts import render
from .models import News

def news(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news/news.html', context)
