from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post<int:pk>/', views.comments, name='comments'),
]