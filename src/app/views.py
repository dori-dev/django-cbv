# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from django.contrib.auth.models import User, Group
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.mixins import LoginRequiredMixin
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


# @method_decorator(login_required, name='dispatch')
class UserList(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = 'app/user-list.html'
    context_object_name = 'users'
    paginate_by = 12

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['users_count'] = User.objects.count()
    #     return context


class UsersGroupList(LoginRequiredMixin, generic.ListView):
    template_name = 'app/user-group-list.html'
    context_object_name = 'users'
    paginate_by = 12

    def get_queryset(self):
        group_name = self.kwargs['group']
        self.group = get_object_or_404(Group, name=group_name)
        return User.objects.filter(
            groups=self.group,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group_name'] = self.group.name
        return context


class UsersGroupAjax(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/user-group-ajax.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


class UsersGroupJson(generic.View):
    def get(self, request: WSGIRequest):
        group_id = request.GET.get('group_id')
        users = User.objects.filter(
            groups=group_id
        ).values('username', 'id')
        return JsonResponse(list(users), safe=False)


class GroupList(LoginRequiredMixin, generic.ListView):
    # queryset = Group.objects.order_by('name')
    model = Group
    template_name = 'app/group-list.html'
    context_object_name = 'groups'
    paginate_by = 12


class GroupDetail(LoginRequiredMixin, generic.DetailView):
    model = Group
    template_name = 'app/group-detail.html'
    # pk_url_kwarg = 'id'


class CreateGroup(LoginRequiredMixin, generic.CreateView):
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


class UpdateGroup(LoginRequiredMixin, generic.UpdateView):
    model = Group
    fields = [
        'name',
        'permissions',
    ]
    template_name = 'app/create-group.html'

    def get_success_url(self) -> str:
        group: Group = self.object
        return reverse('group_detail', args=(group.pk,))


class DeleteGroup(LoginRequiredMixin, generic.DeleteView):
    model = Group
    template_name = 'app/group-confirm-delete.html'
    context_object_name = 'group'
    success_url = reverse_lazy('group_list')


class GroupForm(LoginRequiredMixin, generic.FormView):
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
