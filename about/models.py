from django.db import models
from cloudinary.models import CloudinaryField


# About model
class About(models.Model):
    developer_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
