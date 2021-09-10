from django.contrib import admin
from .models import Topic, Comment


class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "datetime",
        "placed",
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "topic",
        "content",
    )


admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
