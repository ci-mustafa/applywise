from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . import forms
from . import models

def profile(request, pk):
    """
    Display and update the user profile.

    This view retrieves the user profile based on the provided primary key (pk).
    If the user is authenticated, it allows the user to view and update their
    profile information, including username, first name, last name, email,
    and profile image.

    Args:
        request: The HTTP request object containing metadata about the request.
        pk (int): The primary key of the User object to be retrieved.

    Returns:
        HttpResponse: Renders the profile template with user information and forms
        or redirects to the login page if the user is not authenticated.

    Flow:
        - If the user is authenticated, it checks if the request method is POST.
        - If POST, it processes the submitted profile and profile image forms.
        - If the forms are valid, it saves the data and redirects the user
          to their profile page with a success message.
        - If the request method is not POST, it initializes the forms with
          the current user's data and renders the profile template.
    """
    myprofile = get_object_or_404(User, pk=pk)
    profile_image_instance = myprofile.image.first()  # Get the user's profile image
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Initialize forms with request data
            profile_form = forms.ProfileForm(data=request.POST, instance=myprofile)
            profile_image_form = forms.ProfileImageForm(data=request.POST, files=request.FILES, instance=profile_image_instance)
            
            # Check if both forms are valid
            if profile_form.is_valid() and profile_image_form.is_valid():
                profile_form.save()  # Save profile information

                # Save the profile image if it exists
                if profile_image_instance:
                    profile_image_form.save()
                else:
                    # Create a new ProfileImage instance if it does not exist
                    new_image = profile_image_form.save(commit=False)
                    new_image.user = myprofile
                    new_image.save()

                # Add a success message to notify the user
                messages.success(request, f"Dear {request.user}, Your profile has been successfully updated.")
                
                # Redirect the user to their profile page
                return redirect('profile', pk=myprofile.id)
        else:
            # Initialize forms with existing user data
            profile_form = forms.ProfileForm(instance=myprofile)
            profile_image_form = forms.ProfileImageForm(instance=profile_image_instance)

        # Render the profile template with the forms and profile data
        return render(request, 'profile.html', {
            'myprofile': myprofile,
            'profile_form': profile_form,
            'profile_image_form': profile_image_form,
        })
    else:
        # Redirects to the login page if the user is not authenticated
        return redirect('login')




