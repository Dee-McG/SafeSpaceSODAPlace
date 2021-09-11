from django.contrib import admin
from .models import Idea


class IdeaAdmin(admin.ModelAdmin):
    """ Idea message admin """
    list_display = (
        'idea',
    )


admin.site.register(Idea, IdeaAdmin)