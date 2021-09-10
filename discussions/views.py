from django.shortcuts import render
from .models import Topic, Comment

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer, TopicSerializer


def discussions(request):
    """ A view to return the discussions page """
    return render(request, "discussions/discussion.html")


@api_view(['GET'])
def topicList(request):
    """
    REST framework for Django to serialize
    & return all topics in list form.
    """
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def commentList(request):
    """
    REST framework for Django to serialize
    & return all comments in list form.
    """
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)
