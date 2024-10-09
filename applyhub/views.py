from django.shortcuts import render
from . import models

# application list view
def application_list(request):
    # Initialize applications to an empty list by default
    applications = []

    no_application_message = "Currently, there are no applications recorded under your profile."

    # Check if the user is authenticated
    if request.user.is_authenticated:
        applications = models.Application.objects.filter(applicant=request.user)
    return render(request, 'index.html', {"applications": applications,
                                          "no_application_message": no_application_message})

