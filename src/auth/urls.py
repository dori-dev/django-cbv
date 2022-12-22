"""app urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path(
        'register/',
        views.RegisterUser.as_view(),
        name='register'
    ),
    path(
        'user/<int:pk>/',
        views.UserDetail.as_view(),
        name='user_detail'
    ),
]
