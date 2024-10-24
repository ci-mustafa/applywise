from django.shortcuts import render
from . import forms
from . import models

def contact(request):
    contact_form = forms.ContactForm()
    return render(request, 'contact.html', {
        'contact_form': contact_form
    })
