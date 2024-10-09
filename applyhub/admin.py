from django.contrib import admin
from . import models



# Register application model to admin site
@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Application model.
    
    - Displays key fields such as position, company name, position level, date applied, status, and the applicant.
    - Allows searching by position to quickly find applications.
    - Filters the applications by status and creation date for better management in the admin interface.
    - Automatically generates the slug field based on the position field for SEO-friendly URLs.
    """
    list_display = ["position", "company_name", "position_level", "date_applied", "status", "applicant"]
    search_fields = ['position']
    list_filter = ('status','created_on',)
    prepopulated_fields = {'slug': ('position',)}

# Register ProfileImage model to admin site
@admin.register(models.ProfileImage)
class ProfileImageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ProfileImage model.

    - Displays the image and associated user in the admin list view.
    - Enables easy management of profile images directly from the Django admin interface.
    """
    list_display = ['image', 'user']
