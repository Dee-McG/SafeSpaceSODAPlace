from django.conf import settings
from django.db import models


class Topic(models.Model):
    """
    A model for the topics
    All comments belong to a topic.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=2500)
    placed = models.BooleanField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    A model for the comments
    to be collected by the topic.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=2500, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


    def __str__(self):
        return self.content
