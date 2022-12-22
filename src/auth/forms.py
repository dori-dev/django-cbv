from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    # password2 = None

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
        ]
