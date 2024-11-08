from django.contrib import admin
from . import models


# contact model admin
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Customizes the display of the Contact model in the Django admin interface.

    Attributes:
    - list_display: Specifies the fields ('name', 'email', 'message')
      that will be displayed as columns in the contact model list view in the
      admin interface.
      This allows administrators to see the name, email,
      and message of each submission at a glance.
    """
    list_display = ['name', 'email', 'message']
