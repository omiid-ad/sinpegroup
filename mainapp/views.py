from django.shortcuts import render, redirect

from .utils import *
from sinpegroup import settings


def landing(request):
    services = get_services(6)  # 6
    portfolios = get_portfolios(3)  # 3
    land_desc = get_landingpage_desc()
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
    portfolios = get_portfolios('all')
    port_desc = get_port_desc()
    MEDIA_URL = settings.MEDIA_URL
    context = {
        'portfolios': portfolios,
        'port_desc': port_desc,
        'MEDIA_URL': MEDIA_URL,
    }
    return render(request, 'mainapp/portfolio.html', context)
