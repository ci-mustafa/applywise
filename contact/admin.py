from django.contrib import admin
from . import models


# contact model admin
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
