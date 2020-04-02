from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('landing', landing, name="landing"),
    path('about', about, name="about"),
    path('portfolio', portfolio, name="portfolio"),

]
