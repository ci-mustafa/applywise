from django import forms
from . import models


class CreateAppForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = [
            "position", "description", "position_level", 
            "company_name", "date_applied", "status",
            "applied_method", "location", "job_link", 
            "recruiter_contact", "follow_up_date", 
        ]