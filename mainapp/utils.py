from .models import *


def get_crew_members(amount):
    if amount == 'all':
        return Crew.objects.filter(active=True)
    return Crew.objects.filter(active=True)[:amount]


def get_portfolios(amount):
    if amount == 'all':
        return Portfolio.objects.filter(active=True)
    return Portfolio.objects.filter(active=True)[:amount]


def get_services(amount):
    if amount == 'all':
        return Service.objects.filter(active=True)
    return Service.objects.filter(active=True)[:amount]


def get_landingpage_desc():
    return LandingDescription.objects.first()


def get_port_desc():
    return PortfolioDescription.objects.first()
