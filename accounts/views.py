from __future__ import unicode_literals

from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# form that handles authenticating the user
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from . import forms

# Create your views here.

# Do not use at moment


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/login.html"

    # Override get_form which take two arguments
    def get_form(self, form_class = None):
        if form_class is None:
            form_class = self.get_form_class()
        # The first argument of AuthenticationForm is has to be the request
        # so I need to send back self.request and **self.get_form_kwargs()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        # And then, if the form is valid, so they've successfully submitted and
        # the user is a real user then I'm gonna call log in, and pass the
        # request to the login function which is where create the session
        # and then I-m going to call form.get_user())
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    # Redirect back to home
    url = reverse_lazy('home')

    # se dispara cuando entra el request entrante
    def get(self, request, *args, **kwargs):
        # Llamamos a logout with the request
        logout(request)
        return super().get(request, *args, **kwargs)


class SignUpView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        # user = self.request.user
        return context
