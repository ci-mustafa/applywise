from django.shortcuts import render
from . import models

# application list view
def application_list(request):
    """
    Handles the application list view for authenticated users.

    This view retrieves and displays the list of applications submitted by the authenticated user.
    If the user is not authenticated, an empty list of applications is returned, along with a 
    message indicating that no applications are recorded. It also calculates the counts of 
    different application statuses, including 'applied', 'interview', 'offer', and 'rejected'.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: Renders the 'index.html' template with the following context:
            - applications: List of application objects associated with the user.
            - no_application_message: A message indicating no applications if the user has none.
            - application_count: Total count of applications submitted by the user.
            - applied_apps_count: Count of applications with status 'applied'.
            - interview_apps_count: Count of applications with status 'interview'.
            - offered_apps_count: Count of applications with status 'offer'.
            - rejected_apps_count: Count of applications with status 'rejected'.
    """
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

