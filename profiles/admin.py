from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """ User Profile admin """
    list_display = (
        'user',
        'name',
        'organisation',
        'job_title',
    )


admin.site.register(UserProfile, UserProfileAdmin)