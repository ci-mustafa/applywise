from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.application_list, name='home')
]