from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .  import views

def homepage(request):
    return render(request, 'base/homepage.html')

def treatments(request):
    return render(request, 'base/treatments.html', {'title': 'treatments'})  

def products(request):
    return render(request, 'base/products.html', {'title': 'products'})