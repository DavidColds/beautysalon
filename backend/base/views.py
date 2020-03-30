from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def homepage(request):
    return render(request, 'homepage.html')
