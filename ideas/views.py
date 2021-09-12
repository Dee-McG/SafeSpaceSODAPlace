from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, request
from django.views.generic import View

from .models import Board, Idea

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BoardSerializer, IdeaSerializer


class IdeaSummaryView(LoginRequiredMixin, View):
    """"
    A board that shows the ideas
    """
    def get(self, *args, **kwargs):
        try:
            board = Board.objects.get(user=self.request.user, closed=False)
            ideas = Idea.objects.filter(user=self.request.user, closed=False)
            total = 1

            if total < 1:
                message = ('There is no active board')
                messages.warning(self.request, message=message)
                return redirect('profiles.html')
            else:
                context = {
                    'board': board,
                    'total': total,
                    'ideas': ideas,
                }
                return render(self.request, 'ideas/idea.html', context)

        except ObjectDoesNotExist:
            message = ('There is no active board')
            messages.warning(self.request, message=message)
            return redirect('profiles.html')


def board_id(request, pk_board):
    """
    the selected board in the database.
    """
    board = Board.objects.get(id_code=pk_board)
    ideas = Idea.objects.filter(board=pk_board)
    current_user = request.user

    context = {
        'board': board,
        'ideas': ideas,
        'current_user': current_user,
    }
    return render(request, 'ideas/board.html', context)


@api_view(['GET'])
def idea_list(request):
    """
    REST framework for Django to serialize
    & return all ideas in list form.
    """
    ideas = Idea.objects.all()
    serializer = IdeaSerializer(ideas, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def board_create(request):
    """
    REST framework for Django to serialize
    & create an idea board.
    """
    serializer = BoardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def idea_create(request):
    """
    REST framework for Django to serialize
    & create a single idea.
    """
    serializer = IdeaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)