from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Topic, Comment
from ideas.models import Board

from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer


def index(request):
    """
    Renders the discussions index page.
    """
    topic_list = Topic.objects.all()

    try:
        user = request.user
        get_user = get_object_or_404(User, username=user)
        board = Board.objects.get(user=get_user, closed=False)
    except Exception:
        context = {
            'topic_list': topic_list,
        }
        return render(request, 'discussions/discussion.html', context)
    
    board = Board.objects.get(user=get_user, closed=False)
    user = request.user
    get_user = get_object_or_404(User, username=user)
    comments = Comment.objects.all()

    context = {
        'user': user,
        'topic_list': topic_list,
        'board': board,
        'comments': comments,
    }
    return render(request, 'discussions/discussion.html', context)


@api_view(['POST'])
def comment_create(request):
    """
    REST framework for Django to serialize
    & create a single comment.
    """
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
