from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.contrib.messages import get_messages
import os
from .models import Contact 
from . import forms

class ContactViewTests(TestCase):

    def setUp(self):
        """Set up initial data for the contact form tests."""
        self.data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'message': 'This is a test message.'
        }

    def test_contact_view_get(self):
        """Test that the contact page renders correctly with a blank form on GET request."""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertIsInstance(response.context['contact_form'], forms.ContactForm)

    def test_contact_view_post(self):
        """Test that a valid form submission saves data and sends an email."""
        response = self.client.post(reverse('contact'), data=self.data)
        
        # Check that the form data was saved in the database
        self.assertEqual(Contact.objects.count(), 1)
        contact = Contact.objects.first()
        self.assertEqual(contact.name, 'John Doe')
        self.assertEqual(contact.email, 'johndoe@example.com')
        self.assertEqual(contact.message, 'This is a test message.')

        # Check that one email was sent
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        
        # Validate the email contents
        self.assertEqual(email.subject, 'New Contact Form Submission')
        self.assertIn('Name: John Doe', email.body)
        self.assertIn('Email: johndoe@example.com', email.body)
        self.assertIn('Message:\nThis is a test message.', email.body)
        self.assertEqual(email.from_email, os.environ.get('EMAIL_HOST_USER'))

        # Check that a success message was added and that the user was redirected
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("your message has been sent successfully!" in str(m) for m in messages))
        self.assertRedirects(response, reverse('contact'))



  
