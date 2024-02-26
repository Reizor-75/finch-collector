# routes will live in here
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
]