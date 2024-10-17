from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . import forms
from . import models

def profile(request, pk):
    myprofile = get_object_or_404(User, pk=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            profile_form = forms.ProfileForm(data=request.POST, instance=myprofile)
            if profile_form.is_valid():
                profile_form.save()

                # Add a success message to notify the user
                messages.success(request, f"Dear {request.user}, Your profile has been successfully updated.")
                
                # Redirect the user to the 'home' page (or any other appropriate page)
                return redirect('profile', pk=myprofile.id)
        else:
            profile_form = forms.ProfileForm(instance=myprofile)
        return render(request, 'profile.html', {'myprofile': myprofile, 
                                                'profile_form': profile_form})
    else:
        return redirect('login')  # Redirects to the login page



