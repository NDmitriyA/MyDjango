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


DATA = {'omlet': {'яйца, шт': 2, 'молоко, л': 0.1, 'соль, ч.л.': 0.5, },
        'pasta': {'макароны, г': 0.3, 'сыр, г': 0.05, },
        'buter': {'хлеб, ломтик': 1, 'колбаса, ломтик': 1, 'сыр, ломтик': 1,
                  'помидор, ломтик': 1, }, }



def recipes(request, dish):
    servings = int(request.GET.get('servings', 1))
    context = {'recipe': {key: value * servings for key, value in DATA[dish].items()}}
    return render(request, 'app1/index.html', context)