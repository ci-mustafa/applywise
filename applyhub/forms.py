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

        widgets = {
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'position_level': forms.Select(attrs={'class': 'form-select'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_applied': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'applied_method': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'job_link': forms.URLInput(attrs={'class': 'form-control'}),
            'recruiter_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'follow_up_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
    
    