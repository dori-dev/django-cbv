"""app urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path(
        'users/',
        views.UserList.as_view(),
        name='user_list',
    ),
    path(
        'groups/',
        views.GroupList.as_view(),
        name='group_list',
    ),
    path(
        'group/<int:pk>/',
        views.GroupDetail.as_view(),
        name='group_detail',
    ),
    path(
        'create-group/',
        views.CreateGroup.as_view(),
        name='create_group',
    ),
    path(
        'update-group/<int:pk>/',
        views.UpdateGroup.as_view(),
        name='update_group',
    ),
    path(
        'delete-group/<int:pk>/',
        views.DeleteGroup.as_view(),
        name='delete_group',
    ),
]
