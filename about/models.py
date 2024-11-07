from django.db import models
from cloudinary.models import CloudinaryField


# About model
class About(models.Model):
    """
    Model representing the 'About' section of the application.

    Attributes:
        developer_image (CloudinaryField): An image field for storing the developer's image, 
            defaulting to a placeholder image if none is provided.
        title (CharField): The title of the 'About' section, with a maximum length of 100 characters.
        content (TextField): The main content or description of the 'About' section.
        updated_on (DateTimeField): A timestamp indicating the last time this entry was updated, 
            which is automatically updated to the current date and time on each save.
    """
    developer_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
