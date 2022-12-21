"""app urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('groups/', views.GroupList.as_view(), name='group_list'),
    path('group/<int:pk>/', views.GroupDetail.as_view(), name='group_detail'),
]
