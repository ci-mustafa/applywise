from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from . import forms

def contact(request):
    """
    Handle the contact form submission, saving the form data and sending an email.

    This view handles both the display and submission of the contact form. When the form
    is submitted via POST, it validates the form data, saves it to the database, and sends
    an email notification to the site admin containing the contact details. If the email is
    sent successfully, a success message with the sender's name is displayed to the user.
    Otherwise, an error message is displayed.

    Args:
        request: A Django HttpRequest object representing the current HTTP request.

    Returns:
        HttpResponse: The rendered contact page with the form, and success or error messages.
    
    Raises:
        Exception: If there is an issue sending the email, an error message is logged, and 
        the user is redirected back to the contact page.
    
    Context Object:
        contact_form: A Django form instance (ContactForm) that is either empty 
        (for GET requests) or populated with the user's input (for POST requests).
        This form is passed to the template for rendering.
    
    Template:
        contact.html
    """
    if request.method == "POST":
        contact_form = forms.ContactForm(data=request.POST)
        if contact_form.is_valid():
            # Save the form data to the database
            contact_form.save()

            # Prepare email notification
            subject = 'New Contact Form Submission'
            message = (
                f"Name: {contact_form.cleaned_data['name']}\n"
                f"Email: {contact_form.cleaned_data['email']}\n"
                f"Message:\n{contact_form.cleaned_data['message']}"
            )
            from_email = settings.EMAIL_HOST_USER 
            recipient_list = ['akbarimustafa64@gmail.com'] 
            # Create an email message
            email = EmailMessage(
                subject,
                message,
                from_email,
                recipient_list
            )
            # Set the Reply-To header using the extra_headers parameter
            email.extra_headers = {'Reply-To': contact_form.cleaned_data['email']}

            try:
                email.send(fail_silently=False)  # Send the email
                messages.success(request,
                f"Dear {contact_form.cleaned_data['name']}, message sent!")
                return redirect('contact')  
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('contact')

    else:
        contact_form = forms.ContactForm()
    
    return render(request, 'contact.html', {
        'contact_form': contact_form
    })

