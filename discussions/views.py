from django.shortcuts import render


def discussions(request):
    """ A view to return the discussions page """
    return render(request, "discussions/discussion.html")