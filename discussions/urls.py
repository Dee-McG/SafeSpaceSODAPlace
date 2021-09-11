from django.urls import path
from . import views

app_name = 'discussions'

urlpatterns = [
    path('', views.index, name='index'),

    # REST API Url's
    path('list', views.topic_list, name='topic_list'),
    path('details/<str:pk>/', views.topic_details, name='topic_details'),
    path('create/', views.topic_create, name='topic_create'),
    path('update/<str:pk>/', views.topic_update, name='topic_update'),
    path('delete/<str:pk>/', views.topic_delete, name='topic_delete'),
]