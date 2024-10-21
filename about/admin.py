from django.contrib import admin
from . import models


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['developer_image', 'title', 'content', 'updated_on']
