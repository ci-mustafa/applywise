from django.shortcuts import render
from . import models

def about(request):
    about_app = models.About.objects.all().first()
    return render(request, 'about.html', {
        'about_app': about_app
    })
