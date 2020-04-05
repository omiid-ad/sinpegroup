from django.shortcuts import render, redirect

from .utils import *
from sinpegroup import settings


def landing(request):
    services = get_services(6)  # 6
    portfolios = get_portfolios(3, 3)  # 3
    land_desc = get_landingpage_desc()
    MEDIA_URL = settings.MEDIA_URL

    if 'page' in request.GET:
        page_number = request.GET.get('page')
        page_obj = portfolios.get_page(page_number)
    else:
        page_obj = portfolios.get_page(1)
    context = {
        'services': services,
        'portfolios': page_obj,
        'land_desc': land_desc,
        'MEDIA_URL': MEDIA_URL,
    }
    return render(request, 'mainapp/Index.html', context)


def index(request):
    return redirect('landing')


def about(request):
    about_desc = get_about_desc()
    crews = get_crew_members(6)
    MEDIA_URL = settings.MEDIA_URL
    context = {
        'about_desc': about_desc,
        'crews': crews,
        'MEDIA_URL': MEDIA_URL,
    }
    return render(request, 'mainapp/aboutus.html', context)


def portfolio(request):
    portfolios = get_portfolios('all', 5)
    port_desc = get_port_desc()
    MEDIA_URL = settings.MEDIA_URL

    if 'page' in request.GET:
        page_number = request.GET.get('page')
        page_obj = portfolios.get_page(page_number)
    else:
        page_obj = portfolios.get_page(1)

    context = {
        'portfolios': page_obj,
        'port_desc': port_desc,
        'MEDIA_URL': MEDIA_URL,
    }
    return render(request, 'mainapp/portfolio.html', context)
