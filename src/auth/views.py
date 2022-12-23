from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import views
from django.urls import reverse, reverse_lazy
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


class Login(views.LoginView):
    template_name = 'auth/login.html'
    redirect_field_name = None
    # redirect_authenticated_user = True


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
