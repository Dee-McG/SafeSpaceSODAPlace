from django.urls import path
from . import views

app_name = 'discussions'

urlpatterns = [
    path('', views.index, name='index'),

    # REST API Url's
    path('create/', views.comment_create, name='comment_create'),
]