from django.shortcuts import render, get_object_or_404
from ideas.models import Board

from django.contrib.auth.models import User


def index(request):
    """ A view to return the home page """
    
    try:
        user = request.user
        get_user = get_object_or_404(User, username=user)
        board = Board.objects.get(user=get_user, closed=False)
    except Exception:
        return render(request, 'home/index.html')
    
    user = request.user
    get_user = get_object_or_404(User, username=user)

    board = Board.objects.get(user=get_user, closed=False)

    context = {
        'board': board,
        'user': user,
    }
    return render(request, 'home/index.html', context)