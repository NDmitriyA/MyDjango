import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index(request):
    templates_name = 'app1/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, templates_name, context)


def time(request):
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')


def workdir(request):
    dirs = f'{os.listdir()}'

    return HttpResponse(dirs)

