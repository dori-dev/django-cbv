from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import views
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms


class UserDetail(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'auth/user-detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        user: User = super().get_object(queryset)
        user.last_login = now()
        user.save()
        return user


class UserDetailRedirect(LoginRequiredMixin, generic.View):
    model = User

    def get(self, request):
        latest_user = self.model.objects.last()
        return redirect(reverse('user_detail', args=(latest_user.pk,)))


class UserEdit(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = forms.UserEditFrom
    template_name = 'auth/user-edit.html'
    context_object_name = 'user'

    def get_success_url(self) -> str:
        return reverse('user_detail', args=(self.object.pk,))


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


class Login(views.LoginView):
    template_name = 'auth/login.html'
    redirect_field_name = None
    # redirect_authenticated_user = True


class Logout(views.LogoutView):
    template_name = "auth/logout.html"


class ResetPassword(views.PasswordResetView):
    template_name = 'auth/reset-password.html'
    subject_template_name = 'auth/password-reset-subject.txt'
    success_url = reverse_lazy("password_reset_done")


class ResetPasswordDone(generic.TemplateView):
    template_name = 'auth/reset-password-done.html'


class ResetPasswordConfirm(views.PasswordResetConfirmView):
    template_name = 'auth/reset-password-confirm.html'
    success_url = reverse_lazy("password_reset_complete")


class ResetPasswordComplete(generic.TemplateView):
    template_name = 'auth/reset-password-complete.html'
