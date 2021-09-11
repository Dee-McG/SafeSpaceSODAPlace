from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import View

from .models import Board, Idea
from .forms import IdeaForm


class IdeaSummaryView(LoginRequiredMixin, View):
    """"
    A board that shows the ideas
    """
    def get(self, *args, **kwargs):
        try:
            board = Board.objects.get(user=self.request.user, closed=False)
            total = 1

            if total < 1:
                message = ('There is no active order')
                messages.warning(self.request, message=message)
                return redirect('ideas/idea.html')
            else:
                context = {
                    'object': board,
                    'total': total
                }
                return render(self.request, 'ideas/idea.html', context)

        except ObjectDoesNotExist:
            message = ('There is no active order')
            messages.warning(self.request, message=message)
            return redirect('ideas/idea.html')


def create_board(request):
    """
    Creates an idea board to
    places ideas on.
    """
    if request.user.is_anonymous:
        messages.add_message(request, messages.INFO,
                             'Please login to place an idea')
        return redirect('ideas:index')
    else:
        board_querySet = Board.objects.filter(user=request.user, closed=False)

        if board_querySet.exists():
            print('EUREKA')
            board = board_querySet[0]

            messages.info(request, 'Board is already active')
            print('Board already active')
            return redirect('ideas:index')
        else:
            board = Board.objects.create(user=request.user)
            messages.info(request, 'Idea board is created')
            return redirect('ideas:index')