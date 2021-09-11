from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Idea
from .forms import IdeaForm

@login_required
def index(request):
    """ A view to return the ideas page """

    ideas = Idea.objects.all()

    print(ideas)
    context = {
        'ideas' : ideas,
    }
    return render(request, "ideas/idea.html", context)