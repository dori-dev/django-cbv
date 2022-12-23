"""app urls
"""
from django.urls import path
from . import views


urlpatterns = [
    path(
        'user/<int:pk>/',
        views.UserDetail.as_view(),
        name='user_detail',
    ),
    path(
        'register/',
        views.RegisterUser.as_view(),
        name='register',
    ),
    path(
        'login/',
        views.Login.as_view(),
        name='login',
    ),
    path(
        'reset-password/',
        views.ResetPassword.as_view(),
        name='reset_password',
    ),
    path(
        'reset-password-done/',
        views.ResetPasswordDone.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset-password-confirm/<uidb64>/<token>/',
        views.ResetPasswordConfirm.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset-password-complete/',
        views.ResetPasswordComplete.as_view(),
        name='password_reset_complete',
    ),
]
