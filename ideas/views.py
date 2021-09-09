from django.shortcuts import render


def ideas(request):
    """ A view to return the ideas page """
    return render(request, "ideas/idea.html")