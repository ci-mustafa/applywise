from django.test import TestCase
from .forms import ContactForm

class TestContactForm(TestCase):
    def test_form_is_valid(self):
        contact_form = ContactForm({
            'name': "Mustafa",
            "email": "mustafa@gmail.com",
            "message": "This is a message..."
        })
        self.assertTrue(contact_form.is_valid(), msg="Form is not valid")
    
    def test_form_is_not_valid(self):
        contact_form = ContactForm({
            'name': '',
            'email': '',
            'message': ''
        })
        self.assertFalse(contact_form.is_valid(), msg="Form is valid")
        self.assertIn('name', contact_form.errors)
        self.assertIn('email', contact_form.errors)
        self.assertIn('message', contact_form.errors)

    def test_invalid_email_format(self):
        contact_form = ContactForm({
            'name': "Mustafa",
            'email': 'invalid-email-format',
            'message': "This is a message..."
        })
        self.assertFalse(contact_form.is_valid(), msg="Form should be invalid with an incorrect email format")
        self.assertIn('email', contact_form.errors)

    def test_name_too_long(self):
        long_name = 'A' * 61  # Assuming the max length for name is 61
        contact_form = ContactForm({
            'name': long_name,
            'email': "mustafa@gmail.com",
            'message': "This is a message..."
        })
        self.assertFalse(contact_form.is_valid(), msg="Form should be invalid with a name that's too long")
        self.assertIn('name', contact_form.errors)

    def test_valid_email_format(self):
        contact_form = ContactForm({
            'name': "Mustafa",
            'email': "mustafa@gmail.com",
            'message': "This is a valid message."
        })
        self.assertTrue(contact_form.is_valid(), msg="Form should be valid with a proper email format")
