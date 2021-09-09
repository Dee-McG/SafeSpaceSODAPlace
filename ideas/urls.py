from django.urls import path
from . import views


urlpatterns = [
    path('', views.ideas, name='idea'),
]