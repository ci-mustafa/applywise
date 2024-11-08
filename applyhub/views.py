from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


# application list view
@login_required
def application_list(request):
    """
    Handles the application list view for authenticated users.

    This view retrieves and displays the list of applications submitted by the
    authenticated user.
    If the user is not authenticated, an empty list of
    applications is returned, along with a
    message indicating that no applications are recorded.
    It also calculates the counts of
    different application statuses, including 'applied',
    'interview', 'offer', and 'rejected'.

    Args:
        request (HttpRequest): The HTTP request object containing
        metadata about the request.

    Returns:
        HttpResponse: Renders the 'index.html' template with the
        following context:
            - applications: List of application objects
              associated with the user.
            - no_application_message: A message indicating no
              applications if the user has none.
            - application_count: Total count of applications
              submitted by the user.
            - applied_apps_count: Count of applications with status 'applied'.
            - interview_apps_count: Count of applications
              with status 'interview'.
            - offered_apps_count: Count of applications with status 'offer'.
            - rejected_apps_count: Count of applications with
              status 'rejected'.
    """
    # Initialize applications to an empty list by default
    applications = []

    # Initialize counts with default values
    application_count = 0
    applied_apps_count = 0
    interview_apps_count = 0
    offered_apps_count = 0
    rejected_apps_count = 0

    no_application_message = "Currently, there are no applications recorded."

    # Check if the user is authenticated
    if request.user.is_authenticated:
        applications = models.Application.objects.filter(
                        applicant=request.user).order_by("-date_applied")
        # Calculate the total application count
        application_count = applications.count()
        applied_apps_count = applications.filter(
            status="applied".capitalize()).count()
        interview_apps_count = applications.filter(
            status="interview".capitalize()).count()
        offered_apps_count = applications.filter(
            status="offer".capitalize()).count()
        rejected_apps_count = applications.filter(
            status="rejected".capitalize()).count()

        # Pagination
        paginator = Paginator(applications, 5)  # Show 5 applications per page
        page_number = request.GET.get('page')  # Get the page number from
        try:
            applications = paginator.get_page(page_number)
        except PageNotAnInteger:
            applications = paginator.get_page(1)
        except EmptyPage:
            applications = paginator.get_page(paginator.num_pages)

    return render(request, 'index.html',
                  {
                   "applications": applications,
                   "no_application_message": no_application_message,
                   "application_count": application_count,
                   "interview_apps_count": interview_apps_count,
                   "offered_apps_count": offered_apps_count,
                   "rejected_apps_count": rejected_apps_count,
                   "applied_apps_count": applied_apps_count})


# Application creation view
@login_required
def create_application(request):
    """View to handle the creation of a new application.

    This view allows authenticated users to create a new job application.
    If the request method is POST, it validates the submitted form data.
    Upon successful validation, it saves the new application to the database,
    associating it with the logged-in user. If the request method is GET,
    a blank application form is displayed.

    Parameters:
    request (HttpRequest): The HTTP request object containing metadata
    about the request.

    Returns:
    HttpResponse: Redirects to the home page upon successful form submission,
                  or renders the application creation form if the user
                  is authenticated.
                  If the user is not authenticated,
                  it redirects to the login page.
    """
    if request.user.is_authenticated:
        if request.method == "POST":
            application_form = forms.CreateAppForm(data=request.POST)
            if application_form.is_valid():
                # Create a new application instance but don't save it yet
                application = application_form.save(commit=False)

                # Associate the application with the logged-in user
                application.applicant = request.user

                # Authomaticaly fill slug field based on position
                application.slug = slugify(application.position)

                # Save the application to the database
                application.save()

                # Redirect to a success page or back to the application list
                messages.add_message(request, messages.SUCCESS,
                                     message=f"Dear {request.user.username}, \
                                     Your application successfuly created")
                return redirect('home')

        else:
            application_form = forms.CreateAppForm()

        return render(request, 'create_app.html', {
            'application_form': application_form
        })

    else:
        return redirect('account_login')


# Application details view
def application_details(request, pk, slug):
    application = get_object_or_404(models.Application, pk=pk, slug=slug)
    return render(request, "app_details.html", {"application": application})


@login_required
def edit_application(request, pk, slug):
    """
    View to handle editing an existing application.

    This view allows authenticated users to edit their own application.
    The user must be the owner of the application they are trying to edit.
    If the form is submitted via POST, the application will be updated with
    the new data. If the request is GET, the form will be prepopulated with
    the current application data.

    Args:
        request (HttpRequest): The HTTP request object,
        which contains metadata about the request.
        pk (int): The primary key (ID) of the application that
        the user wants to edit.

    Returns:
        HttpResponse:
        - If the user is authenticated and is the owner of the application,
          it returns a rendered HTML page with the prepopulated form
          for editing.
        - If the form is valid (POST), the updated application is saved,
          and the user is redirected.
        - If the user is not authenticated or is not the owner of
          the application, they are redirected to the login page or any
          other appropriate error page.

    Raises:
        Http404: If the application with the provided
        primary key does not exist.
    """

    # Fetch the application object by primary key (pk), or return 404
    application = get_object_or_404(models.Application, pk=pk, slug=slug)

    # Check if the logged-in user is the owner of the application
    if request.user.is_authenticated and application.applicant == request.user:

        # If the request method is POST, process the form data for updating
        if request.method == "POST":
            # Create the form with the POST data and the instance (for editing)
            application_form = forms.CreateAppForm(data=request.POST,
                                                   instance=application)

            # Validate the form
            if application_form.is_valid():
                # Save the updated application to the database

                # Authomaticaly fill slug field based on position
                application.slug = slugify(application.position)

                application_form.save()

                # Add a success message to notify the user
                messages.success(request, f"Dear {request.user}, \
                Your application has been successfully updated.")
                # Redirect the user to the 'home' page
                return redirect('home')

        else:
            # For a GET request, prepopulate the form with the existing data
            application_form = forms.CreateAppForm(instance=application)

        # Render the edit page with the prepopulated form
        return render(request, 'edit_app.html', {
            'application_form': application_form,
            'application': application
        })

    else:
        # If the user is not authenticated
        return redirect('account_login')


# Delete application view
@login_required
def delete_application(request, pk, slug):

    """
    View function to delete a specific job application
    for an authenticated user.

    This view retrieves an application based on its primary key (pk),
    (Slug just shows the name of the application) ensuring that the application
    exists and belongs to the currently authenticated user.
    If condition is met, the application is deleted.
    If the user is not authenticated or does not own the application,
    they are redirected to the login page.

    Args:
        request (HttpRequest): The HTTP request object containing metadata
        about the request, including the user data.
        pk (int): The primary key of the application to be deleted.
        slug (str): The slug of the application.

    Returns:
        HttpResponseRedirect: A redirection to the 'home' page if the
        application is successfully deleted or to the login page if the user
        is not authenticated or authorized.

    Raises:
        Http404: If the application does not exist or cannot be
        found based on the provided `pk`.

    Example:
        - A user attempts to delete an application with a
          given primary key (pk). If they own the application and are
          logged in, it will be deleted, and they will be redirected to the
          homepage with a success message.
        - If the user is not authenticated or does not own the application,
          they will be redirected to the login page.
    """
    application = get_object_or_404(models.Application, pk=pk, slug=slug)
    if request.user.is_authenticated and application.applicant == request.user:
        application.delete()
        # Add a success message to notify the user
        messages.success(request, f"Dear {request.user}, \
        Your application has been successfully deleted.")
        # Redirect the user to the 'home' page (or any other appropriate page)
        return redirect('home')

    else:
        # If the user is not authenticated
        return redirect('account_login')


# Search view
@login_required
def search_applications(request):

    """
    View function to search applications based on a query input from the user.

    This view retrieves all applications for the current authenticated user,
    and if a query is provided, it filters the applications by matching the
    search term against several fields: `position`, `position_level`,
    `status`, or `company_name`.
    The filtered results are then rendered in the 'search.html' template.

    Args:
        request (HttpRequest): The HTTP request object containing metadata
        about the request, including the GET parameters with the search
        term (query) and the user information.

    Returns:
        HttpResponse: The rendered 'search.html' page displaying the
        filtered list of applications that match the search criteria for
        the logged-in user.

    Template:
        search.html: A template that displays the search
        results for the applications.

    Example:
        - A user searches for "Junior" in the search form. The search
          will return all applications where the `position`, `position_level`,
          `status`, or `company_name` contains the term "Junior".
        - If no query is provided, it returns all applications
        for the current user.
    """

    query = request.GET.get('query', '')  # Get the search term from the input
    filtered_applications = models.Application.objects.filter(
        applicant=request.user)

    if query:
        # Filter by `position`, `position_level`, `status`, or `company_name`
        filtered_applications = filtered_applications.filter(
            Q(position__icontains=query) |
            Q(position_level__icontains=query) |
            Q(status__icontains=query) |
            Q(company_name__icontains=query)
        )

    return render(request, 'search.html',
                  {'applications': filtered_applications, 'query': query})


# Filter view
@login_required
def filter_apps(request, status):

    """
    View function to filter applications based on their status and
    the current logged-in user.

    This view retrieves applications for the current authenticated user,
    filtering them by the specified status (e.g.,'Applied', 'Interview',
    'Offered', 'Rejected').
    The results are displayed on the 'filter.html' template.

    Args:
        request (HttpRequest): The HTTP request object, which contains
        metadata about the request, including user information.
        status (str): The status of the applications to filter by
        (e.g.,'Applied', 'Interview', 'Offered', 'Rejected').

    Returns:
        HttpResponse: The rendered 'filter.html' page displaying the filtered
        list of applications for the user, along with the selected status.

    Template:
        filter.html: A template that displays a list of applications
        filtered by the selected status.

    Example:
        - URL to trigger this view: /applications/filter/Interview/
        - It will show all applications where the status is 'Interview'
          for the logged-in user.
    """
    apps = models.Application.objects.filter(applicant=request.user,
                                             status=status)
    return render(request, 'filter.html', {'apps': apps,
                                           'status': status})
