from django.urls import path, include
from . import views

urlpatterns = [
   path('profile/<int:pk>', views.profile, name='profile')
]