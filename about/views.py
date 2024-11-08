from django.shortcuts import render
from . import models


def about(request):
    """
    Render the 'About' page with application information.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'about.html' template
        with context data.
    """
    about_app = models.About.objects.all().first()
    return render(request, 'about.html', {
        'about_app': about_app
    })
