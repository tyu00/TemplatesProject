from django.http import HttpResponse
from django.shortcuts import render

from . import models


def index(request):
    news = models.News.objects.all()
    return render(request, template_name='news/index.html', context={'news': news, 'title': 'Список новостей'})
