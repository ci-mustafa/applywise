from django.shortcuts import render
from . import models

# application list view
def application_list(request):
    # Initialize applications to an empty list by default
    applications = []

    # Initialize counts with default values
    application_count = 0
    applied_apps_count = 0
    interview_apps_count = 0
    offered_apps_count = 0
    rejected_apps_count = 0

    no_application_message = "Currently, there are no applications recorded under your profile."

    # Check if the user is authenticated
    if request.user.is_authenticated:
        applications = models.Application.objects.filter(applicant=request.user)
        application_count = applications.count()
        applied_apps_count = applications.filter(status="applied".capitalize()).count()
        interview_apps_count = applications.filter(status="interview".capitalize()).count()
        offered_apps_count = applications.filter(status="offer".capitalize()).count()
        rejected_apps_count = applications.filter(status="rejected".capitalize()).count()
    return render(request, 'index.html', {"applications": applications,
                                          "no_application_message": no_application_message,
                                          "application_count": application_count,
                                          "interview_apps_count": interview_apps_count,
                                          "offered_apps_count": offered_apps_count,
                                          "rejected_apps_count": rejected_apps_count,
                                          "applied_apps_count": applied_apps_count})

