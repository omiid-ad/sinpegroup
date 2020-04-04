from .models import *


def get_crew_members():
    return Crew.objects.filter(active=True)[:6]
