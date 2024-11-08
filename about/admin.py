from django.contrib import admin
from . import models


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    """
    Admin configuration for the About model.

    This class defines how the About model will be displayed in
    the Django admin interface.
    It specifies which fields will be shown in the list display
    and can be customized further
    to allow filtering, searching, and other administrative functions.

    Attributes:
        list_display (list): A list of model fields to display
        in the admin list view.
    """
    list_display = ['developer_image', 'title', 'content', 'updated_on']
