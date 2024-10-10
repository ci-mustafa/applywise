from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.application_list, name='home'),
   path('create_application', views.create_application, name="create-application")
]