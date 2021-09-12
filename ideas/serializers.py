from rest_framework import serializers
from .models import Board, Idea


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = (
            'id_code',
            'date',
            'user',
            'closed',
        )


class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = (
            
            'user',
            'closed',
            'idea_message',
            'board',
        )