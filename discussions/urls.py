from django.urls import path
from . import views

app_name = 'discussions'

urlpatterns = [
    path('', views.discussions, name='discussion'),

    # REST API Url's
    path('list', views.topicList, name='topicList'),
]