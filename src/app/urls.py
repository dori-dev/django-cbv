"""app urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list')
]
