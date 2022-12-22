# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views import generic
from django.urls import reverse, reverse_lazy
from .import forms

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


class DeleteGroup(generic.DeleteView):
    model = Group
    template_name = 'app/group-confirm-delete.html'
    context_object_name = 'group'
    success_url = reverse_lazy('group_list')


class GroupForm(generic.FormView):
    form_class = forms.GroupForm
    template_name = 'app/create-group.html'

    def form_valid(self, form):
        group = Group.objects.create(
            name=form.cleaned_data["name"],
        )
        group.permissions.set(form.cleaned_data["permissions"])
        self.pk = group.pk
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('group_detail', args=(self.pk,))
