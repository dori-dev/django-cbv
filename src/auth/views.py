from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse
# from django.shortcuts import redirect
from . import forms


class UserDetail(generic.DetailView):
    model = User
    template_name = 'auth/user-detail.html'
    context_object_name = 'user'


class RegisterUser(generic.CreateView):
    model = User
    # fields = [
    #     'first_name',
    #     'last_name',
    #     'username',
    #     'password',
    # ]
    form_class = forms.UserRegisterForm
    template_name = 'auth/register.html'

    # def form_valid(self, form):
    #     user: User = form.save(commit=False)
    #     user.set_password(form.cleaned_data['password'])
    #     user.save()
    #     return redirect(reverse('user_detail', args=(user.pk,)))

    def get_success_url(self) -> str:
        return reverse('user_detail', args=(self.object.pk,))


class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_field_name = None
    redirect_authenticated_user = True
