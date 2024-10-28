from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Application 

class ApplicationListViewTests(TestCase):
    """
    Test suite for the application list view to ensure that
    authenticated users can view their applications.
    """

    def setUp(self):
        """
        Set up the test environment, creating a user and their application.
        """
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create an application for the user
        self.application = Application.objects.create(
            position='Software Developer',
            description='Develop software applications.',
            slug='software-developer',
            position_level='Junior',
            company_name='Tech Company',
            date_applied='2024-10-28',
            status='Applied',
            applied_method='Website',
            location='Remote',
            job_link='http://example.com/job',
            recruiter_contact='recruiter@example.com',
            follow_up_date='2024-11-28',
            applicant=self.user  # Link application to the user
        )

    def test_application_list_view_for_authenticated_user(self):
        """
        Test that an authenticated user can view their applications.
        """
        # Log the user in
        self.client.login(username='testuser', password='testpassword')
        
        # Get the application list view
        response = self.client.get(reverse('home'))
        
        # Check that the response is successful (HTTP 200)
        self.assertEqual(response.status_code, 200)
        
        # Verify that the application is in the context
        self.assertIn('applications', response.context)
        
        # Check that the application count in the context is correct
        self.assertEqual(response.context['application_count'], 1)
        
        # Check that the applications returned include the one created in setUp
        self.assertEqual(len(response.context['applications']), 1)
        self.assertEqual(response.context['applications'][0], self.application)
        
        # check the presence of the no_application_message
        self.assertNotIn("Currently, there are no applications recorded under your profile.", response.content.decode())

    def test_application_list_view_for_unauthenticated_user(self):
        """
        Test that an unauthenticated user cannot view the application list.
        """
        # Get the application list view without logging in
        response = self.client.get(reverse('home'))
        
        # Check that the response is a redirect to the login page
        self.assertRedirects(response, '/accounts/login/?next=/')
