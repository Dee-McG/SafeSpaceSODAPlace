from django.urls import path
from . import views


urlpatterns = [
    path('', views.discussions, name='discussion'),
]