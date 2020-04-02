from django.urls import path
from . import views
from .views import homepage
from django.contrib import admin
from django.urls import path

from .views import homepage

urlpatterns = [
    path('', views.homepage, name='base-home'),
    path('treatments/', views.treatments, name='base-treatments'),
    path('products/', views.products, name='base-products'),
]