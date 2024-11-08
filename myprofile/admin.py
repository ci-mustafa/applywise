from django.contrib import admin
from . import models


# Register ProfileImage model to admin site
@admin.register(models.ProfileImage)
class ProfileImageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ProfileImage model.

    - Displays the image and associated user in the admin list view.
    - Enables easy management of profile images directly from
      the Django admin interface.
    """
    list_display = ['image', 'user']