from django.test import TestCase
from .forms import ContactForm

class TestContactForm(TestCase):
    """
    Test suite for the ContactForm class to ensure proper validation and
    behavior of the form fields.

    This includes tests for valid submissions, invalid submissions,
    email format validation, name length restrictions, and correct
    error messages for different failure scenarios.
    """

    def test_form_is_valid(self):
        """
        Test that the form is valid with proper data.

        This test checks that the form can successfully validate when
        provided with a name, email, and message.
        """
        contact_form = ContactForm({
            'name': "Mustafa",
            "email": "mustafa@gmail.com",
            "message": "This is a message..."
        })
        self.assertTrue(contact_form.is_valid(), msg="Form is not valid")
    
    def test_form_is_not_valid(self):
        """
        Test that the form is invalid when no data is provided.

        This test checks that the form raises validation errors for
        empty fields and that the appropriate fields are flagged as
        containing errors.
        """
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
        """
        Test that the form is invalid with an incorrectly formatted email.

        This test verifies that the form does not validate when the
        email format is not correct and that an error is raised on
        the email field.
        """
        contact_form = ContactForm({
            'name': "Mustafa",
            'email': 'invalid-email-format',
            'message': "This is a message..."
        })
        self.assertFalse(contact_form.is_valid(), msg="Form should be invalid with an incorrect email format")
        self.assertIn('email', contact_form.errors)

    def test_name_too_long(self):
        """
        Test that the form is invalid when the name exceeds maximum length.

        This test checks that the form raises a validation error when
        the name provided exceeds the allowed length.
        """
        long_name = 'A' * 61  # Assuming the max length for name is 61
        contact_form = ContactForm({
            'name': long_name,
            'email': "mustafa@gmail.com",
            'message': "This is a message..."
        })
        self.assertFalse(contact_form.is_valid(), msg="Form should be invalid with a name that's too long")
        self.assertIn('name', contact_form.errors)

    def test_valid_email_format(self):
        """
        Test that the form is valid with a properly formatted email.

        This test checks that the form successfully validates when a
        valid email format is provided along with a name and message.
        """
        contact_form = ContactForm({
            'name': "Mustafa",
            'email': "mustafa@gmail.com",
            'message': "This is a valid message."
        })
        self.assertTrue(contact_form.is_valid(), msg="Form should be valid with a proper email format")

