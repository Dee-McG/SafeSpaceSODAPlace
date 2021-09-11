from django import forms
from .models import Idea


class IdeaForm(forms.ModelForm):
    """ Form for user to add an idea message, takes in idea-message field """
    class Meta:
        model = Idea
        fields = ['idea_message']