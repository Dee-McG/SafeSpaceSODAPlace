from rest_framework import serializers
from .models import Topic, Comment


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = (
            'title',
            'description',
            'placed',
            'datetime',
            'voting',
        )
        depth = 1


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'topic',
            'content',
        )