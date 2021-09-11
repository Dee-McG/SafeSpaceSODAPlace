from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', views.index, name='index'),
]