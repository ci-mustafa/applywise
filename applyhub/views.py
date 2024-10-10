from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from . import forms

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

# Application creation view
def create_application(request):
    """View to handle the creation of a new application.

    This view allows authenticated users to create a new job application.
    If the request method is POST, it validates the submitted form data.
    Upon successful validation, it saves the new application to the database,
    associating it with the logged-in user. If the request method is GET,
    a blank application form is displayed.

    Parameters:
    request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
    HttpResponse: Redirects to the home page upon successful form submission,
                  or renders the application creation form if the user is authenticated.
                  If the user is not authenticated, it redirects to the login page.
    """
    if request.user.is_authenticated:
        if request.method == "POST":
            application_form = forms.CreateAppForm(data=request.POST)
            if application_form.is_valid():
                # Create a new application instance but don't save it yet
                application = application_form.save(commit=False)
                
                # Associate the application with the logged-in user
                application.applicant = request.user  # Assuming you have an applicant field in your model
                
                # Save the application to the database
                application.save()

                # Redirect to a success page or back to the application list
                messages.add_message(request, messages.SUCCESS, 
                message=f"Dear {request.user.username}, Your application successfuly created")
                return redirect('home')  

        else:
            application_form = forms.CreateAppForm()  # Create a blank form for GET request

        return render(request, 'create_app.html', {
            'application_form': application_form
        })

    else:
        return redirect('account_login')  # Redirect to login if the user is not authenticated

