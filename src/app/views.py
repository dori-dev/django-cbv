from django.contrib.auth.models import User, Group
from django.views import generic


class UserList(generic.ListView):
    model = User
    template_name = 'app/user-list.html'
    context_object_name = 'users'


class GroupList(generic.ListView):
    model = Group
    template_name = 'app/group-list.html'
    context_object_name = 'groups'
