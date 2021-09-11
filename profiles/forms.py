from django import forms
from .models import UserProfile


class EditProfileForm(forms.ModelForm):
    """ Form for user to edit profile that uses all fields """
    class Meta:
        model = UserProfile
        fields = ['name', 'organisation', 'job_title']