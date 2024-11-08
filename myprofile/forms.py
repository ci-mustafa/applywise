from django import forms
from . import models


class ProfileForm(forms.ModelForm):
    """
    A form for updating user profile information.

    This form is associated with the User model and allows users
    to update their username, first name, last name, and email address.

    Attributes:
        username: A field for the user's username, styled with
                  Bootstrap classes and a placeholder.
        first_name: A field for the user's first name, styled with
                    Bootstrap classes and a placeholder.
        last_name: A field for the user's last name, styled with
                   Bootstrap classes and a placeholder.
        email: A field for the user's email address, styled with
               Bootstrap classes and a placeholder.
    """

    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control custom-input',
                       'placeholder': 'Username'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control custom-input',
                       'placeholder': 'First Name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control custom-input',
                       'placeholder': 'Last Name'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control custom-input',
                       'placeholder': 'Email'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Initializes the ProfileForm instance.
        """
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None  # Remove help text


class ProfileImageForm(forms.ModelForm):
    """
    A form for uploading a user's profile image.

    This form is associated with the ProfileImage model and allows
    users to upload a new profile picture.

    Attributes:
        image: A field for the user's profile image, styled with
               Bootstrap classes.
    """

    class Meta:
        model = models.ProfileImage
        fields = ['image']

        widgets = {
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control-file', 'id': 'id_image'}),
        }
