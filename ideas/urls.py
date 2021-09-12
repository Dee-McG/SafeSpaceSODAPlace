from django.urls import path
from . import views
from .views import IdeaSummaryView

app_name = 'ideas'

urlpatterns = [
    path('board/', IdeaSummaryView.as_view(), name='board'),

    # REST API Url's
    path('list/', views.idea_list, name='idea_list'),
    path('create/', views.idea_create, name='idea_create'),
]