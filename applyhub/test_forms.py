from django.test import TestCase
from .forms import CreateAppForm


# Tests for application form
class TestApplicationForm(TestCase):
    def test_form_is_valid_with_valid_data_but_have_null_fields(self):
        """
        Test that the form is valid when essential required fields are filled,
        but optional fields ('description', 'job_link',
        and 'recruiter_contact')
        are left empty.
        This verifies that optional fields can be left blank while maintaining
        form validity as long as all required fields contain valid data.
        """
        application_form = CreateAppForm({
            'position': 'software developer',
            'description': '',
            'position_level': 'Junior',
            'company_name': 'martin',
            'date_applied': '2024-10-28',
            'status': 'Applied',
            'applied_method': 'Website',
            'location': 'muich',
            'job_link': '',
            'recruiter_contact': '',
            'follow_up_date': '2024-10-28'
        })
        self.assertTrue(application_form.is_valid(), msg='Form is not valid')

    def test_form_is_valid_with_valid_data(self):
        """
        Test that the form is valid when all fields, including optional fields,
        are provided with appropriate data.

        This test confirms the form's validity under ideal conditions where all
        fields contain data, ensuring that the form handles both required and
        optional fields correctly with valid input.
        """
        application_form = CreateAppForm({
            'position': 'software developer',
            'description': 'This is a position for ...',
            'position_level': 'Junior',
            'company_name': 'martin',
            'date_applied': '2024-10-28',
            'status': 'Applied',
            'applied_method': 'Website',
            'location': 'muich',
            'job_link': 'https://www.linkedin.com/jobs/',
            'recruiter_contact': '01795253045',
            'follow_up_date': '2024-10-28'
        })
        self.assertTrue(application_form.is_valid(), msg='Form is not valid')




