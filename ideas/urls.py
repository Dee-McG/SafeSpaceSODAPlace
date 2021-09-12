from django.urls import path
from . import views
from .views import IdeaSummaryView

app_name = 'ideas'

urlpatterns = [
    path('board/', IdeaSummaryView.as_view(), name='board'),
    path('grab/', views.grab_ideas, name='grab_ideas'),

    # REST API Url's
    path('list/', views.idea_list, name='idea_list'),
    path('board/<str:pk_board>/', views.board_id, name='board_id'),
    path('create/', views.idea_create, name='idea_create'),
    path('board_create/', views.board_create, name='board_create'),
]