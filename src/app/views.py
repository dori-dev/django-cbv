# from django.shortcuts import render
# from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.views import generic
from django.urls import reverse


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
    # queryset = Group.objects.order_by('name')
    model = Group
    template_name = 'app/group-list.html'
    context_object_name = 'groups'
    paginate_by = 12


class GroupDetail(generic.DetailView):
    model = Group
    template_name = 'app/group-detail.html'
    # pk_url_kwarg = 'id'


class CreateGroup(generic.CreateView):
    model = Group
    fields = [
        'name',
        'permissions',
    ]
    template_name = 'app/create-group.html'
    # initial = {
    #     'name': 'group name...'
    # }
    # success_url = reverse_lazy('group_list')

    def get_success_url(self) -> str:
        group: Group = self.object
        return reverse('group_detail', args=(group.pk,))


class UpdateGroup(generic.UpdateView):
    model = Group
    fields = [
        'name',
        'permissions',
    ]
    template_name = 'app/create-group.html'

    def get_success_url(self) -> str:
        group: Group = self.object
        return reverse('group_detail', args=(group.pk,))
