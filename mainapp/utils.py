from django.core.paginator import Paginator

from .models import *


def get_crew_members(amount):
    if amount == 'all':
        return Crew.objects.filter(active=True)
    return Crew.objects.filter(active=True)[:amount]


def get_portfolios(amount, paginated_by):
    if amount == 'all':
        portfolios = Portfolio.objects.filter(active=True).order_by('-date_created')
    else:
        portfolios = Portfolio.objects.filter(active=True).order_by('-date_created')[:amount]
    if paginated_by:
        paginator = Paginator(portfolios, paginated_by)
        return paginator


def get_services(amount):
    if amount == 'all':
        return Service.objects.filter(active=True)
    return Service.objects.filter(active=True)[:amount]


def get_landingpage_desc():
    return LandingDescription.objects.first()


def get_port_desc():
    return PortfolioDescription.objects.first()


def get_about_desc():
    return AboutUsDescription.objects.first()
