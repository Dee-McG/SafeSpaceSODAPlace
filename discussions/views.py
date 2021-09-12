from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Topic, Comment
from ideas.models import Board

from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer, TopicSerializer


def index(request):
    """
    Renders the discussions index page.
    """
    topic_list = Topic.objects.all()
    user = request.user
    get_user = get_object_or_404(User, username=user)

    try:
        board = Board.objects.get(user=get_user, closed=False)
    except Exception:
        context = {
            'topic_list': topic_list,
        }
        return render(request, 'discussions/discussion.html', context)
    
    board = Board.objects.get(user=get_user, closed=False)

    context = {
        'topic_list': topic_list,
        'board': board,
    }
    return render(request, 'discussions/discussion.html', context)


@api_view(['GET'])
def topic_list(request):
    """
    REST framework for Django to serialize
    & return all topics in list form.
    """
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def topic_details(request, pk):
    """
    REST framework for Django to serialize
    & return a single topic details.
    """
    topic = Topic.objects.get(id=pk)
    serializer = TopicSerializer(topic, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def topic_create(request):
    """
    REST framework for Django to serialize
    & create a single topic.
    """
    serializer = TopicSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def topic_update(request, pk):
    """
    REST framework for Django to serialize
    & update a single topic details.
    """
    topic = Topic.objects.get(id=pk)
    serializer = TopicSerializer(instance=topic, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def topic_delete(request, pk):
    """
    REST framework for Django to serialize
    & delete a single topic.
    """
    topic = Topic.objects.get(topic_id=pk)
    topic.delete()

    messages.warning(request,('The topic is removed'))

    return Response('The topic is removed')


@api_view(['GET'])
def commentList(request):
    """
    REST framework for Django to serialize
    & return all comments in list form.
    """
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data)
