from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class UserRegisterForm(UserCreationForm):
    # password2 = None

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
        ]


class UserEditFrom(forms.ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = User
        fields = [
            'groups',
            'first_name',
            'last_name',
            'email',
            'username',
        ]
