from django.contrib import admin
from .models import Board, Idea


class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'id_code',
        'user',
        'date',
        'closed',
    )


class IdeaAdmin(admin.ModelAdmin):
    list_display = (
        'board',
        'user',
        'idea_message',
        'closed',
    )


admin.site.register(Board, BoardAdmin)
admin.site.register(Idea, IdeaAdmin)