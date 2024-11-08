from django.test import TestCase
from django.urls import reverse
from .models import About


class AboutViewTests(TestCase):

    def setUp(self):
        """Create a test About object to be used in the tests."""
        self.about_instance = About.objects.create(
            developer_image='path/to/image.jpg',
            title='About Us',
            content='This is the about page content.'
        )

    def test_about_view(self):
        """Test that the about view returns the correct
           template and context."""
        response = self.client.get(reverse('about'))

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, 'about.html')

        # Check that the context contains the About instance
        self.assertEqual(response.context['about_app'], self.about_instance)


