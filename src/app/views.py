# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views import generic


# class UserList(generic.View):
#     def get(self, request, *args, **kwargs):
#         users = User.objects.all()
#         context = {
#             'users': users,
#         }
#         return render(request, 'app/user-list.html', context)


# class UserList(generic.base.TemplateView):
#     template_name = 'app/user-list.html'
#     extra_context = {
#         'users': User.objects.all(),
#     }


class UserList(generic.ListView):
    model = User
    template_name = 'app/user-list.html'
    context_object_name = 'users'
    paginate_by = 12


class GroupList(generic.ListView):
    model = Group
    template_name = 'app/group-list.html'
    context_object_name = 'groups'
    paginate_by = 12
