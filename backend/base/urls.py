from django.urls import path
from . import views
from .views import homepage
from django.contrib import admin
from django.urls import path

app_name =  "main"

from .views import homepage

urlpatterns = [
    path('', views.homepage, name='base-home'),
]