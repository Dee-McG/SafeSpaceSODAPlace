from django.shortcuts import render


def index(request):
    """ A view to return the ideas page """
    return render(request, "ideas/idea.html")