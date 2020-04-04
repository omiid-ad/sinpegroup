from django.shortcuts import render, redirect

from .utils import *
from sinpegroup import settings


def landing(request):
    services = get_services()  # 6
    portfolios = get_portfolios()  # 3
    land_desc = get_landingpage_desc()  # 1
    MEDIA_URL = settings.MEDIA_URL
    context = {
        'services': services,
        'portfolios': portfolios,
        'land_desc': land_desc,
        'MEDIA_URL': MEDIA_URL,
    }
    return render(request, 'mainapp/Index.html', context)


def index(request):
    return redirect('landing')


def about(request):
    return render(request, 'mainapp/aboutus.html')


def portfolio(request):
    return render(request, 'mainapp/portfolio.html')
