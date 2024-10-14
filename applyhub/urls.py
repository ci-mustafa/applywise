from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.application_list, name='home'),
   path('create_application', views.create_application, name="create-application"),
   path('application_details/<int:pk>/<slug:slug>', views.application_details, name="application-details"),
   path('edit_application/<int:pk>/<slug:slug>', views.edit_application, name="edit-application"),
   path('delete_application/<int:pk>/<slug:slug>', views.delete_application, name="delete-application"),
]