from django.urls import path
from .views import IdeaSummaryView

app_name = 'ideas'

urlpatterns = [
    path('board/', IdeaSummaryView.as_view(), name='board'),
]