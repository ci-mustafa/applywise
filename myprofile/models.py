from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

#############################
#### Profile image model ####
#############################
class ProfileImage(models.Model):
    """
    Model to store a user's profile image.

    - The 'image' field stores the profile image in Cloudinary
      with a default placeholder if no image is provided.
    - The 'user' field establishes a foreign key relationship with the User model, 
      linking each profile image to a specific user.
    - The 'related_name' allows reverse lookups from the User model to access their associated profile image.
    """
    image = CloudinaryField('image', default='placeholder')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image')