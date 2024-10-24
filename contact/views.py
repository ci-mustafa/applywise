from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from . import models

def contact(request):
    if request.method == "POST":
        contact_form = forms.ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  
    else:
        contact_form = forms.ContactForm()
    return render(request, 'contact.html', {
        'contact_form': contact_form
    })
