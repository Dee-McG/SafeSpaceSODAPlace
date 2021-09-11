from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Idea(models.Model):
    """
    A model to save and display chat messages
    """
    idea = models.CharField(max_length=80,
                            null=False, blank=False)
    idea_message = models.CharField(max_length=2500,
                               null=False, blank=False)


    def __str__(self):
        return self.idea_message