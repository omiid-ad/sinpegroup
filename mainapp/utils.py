from .models import *


def get_crew_members():
    return Crew.objects.filter(active=True)[:6]


def get_portfolios():
    return Portfolio.objects.filter(active=True)[:3]


def get_services():
    return Service.objects.filter(active=True)[:6]


def get_landingpage_desc():
    return LandingDescription.objects.first()
