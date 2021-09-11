from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import EditProfileForm
from .models import UserProfile
from ideas.models import Board
from django.contrib.auth.models import User


@login_required
def profiles(request, user):
    """ A view to return the profile page """

    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    context = {
        'user': user,
    }

    try:
        get_user = get_object_or_404(User, username=user)

        user_profile = get_object_or_404(UserProfile, user=get_user)
        board_list = request.user.board_set.get()

        context = {
                'user_profile': user_profile,
                'user': user,
                'board_list': board_list,
            }

        return render(request, 'profiles/profile.html', context)
    except Exception:
        return render(request, 'profiles/profile.html', context)


@login_required
def edit_profile(request, user):
    """ A function to edit the users profile and render
    the edit_profile page """

    try:
        profile = get_object_or_404(UserProfile, user=request.user)
    except Exception:
        # Create empty User Profile if it doesn't exist
        UserProfile.objects.create(
            user=request.user, name='')

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect(reverse('profiles', args=[user]))
        else:
            messages.error(request,
                           'Profile update failed.'
                           'Please ensure the form is valid!')

    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profiles/edit_profile.html', context)
