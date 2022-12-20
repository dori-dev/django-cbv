from django.contrib.auth.models import User
from django.views import generic


class UserList(generic.ListView):
    model = User
    template_name = 'app/user-list.html'
    context_object_name = 'users'
