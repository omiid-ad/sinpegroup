from django.shortcuts import render, redirect


def landing(request):
    return render(request, 'mainapp/Index.html')


def index(request):
    return redirect('landing')


def about(request):
    return render(request, 'mainapp/aboutus.html')


def portfolio(request):
    return render(request, 'mainapp/portfolio.html')
