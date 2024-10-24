from django import forms
from . import models

# contact form
class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name', 'email', 'message']
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Your Name', 
            'class': 'form-control',  
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Your Email',  
            'class': 'form-control',  
        })
        self.fields['message'].widget.attrs.update({
            'placeholder': 'Your Message',  
            'class': 'form-control',  
        })
    
        # Set labels to empty strings
        self.fields['name'].label = ''
        self.fields['email'].label = ''
        self.fields['message'].label = ''