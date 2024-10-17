from django import forms
from . import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email']
    

    # Override the help text
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None  # Remove help text