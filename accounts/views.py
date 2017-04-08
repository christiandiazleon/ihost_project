from __future__ import unicode_literals

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
# form that handles authenticating the user
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.shortcuts import render

from . import forms
from .models import StudentProfile, ProfessorProfile, ExecutiveProfile

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


def signup(request):
    form = forms.UserCreateForm(request.POST or None)
    # success_url = reverse_lazy("dashboard")
    if form.is_valid():
        saved_user = form.save()
        # We going authenticate the user through django authenticate method
        # which receive the user captured and the password sent in the
        # registration form in forms.py-UserCreateForm
        user = authenticate(username = saved_user.username,
                            password = form.cleaned_data['password1'])

        # Login the user, then we authenticate it
        login(request,user)
        # redirect the user to the url home or profile
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        return render(request, 'accounts/signup2.html', {'form': form})


class DashboardProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardProfileView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_student:
            profile = user.get_student_profile()
            context['userprofile'] = profile

        elif user.is_professor:
            profile = user.get_professor_profile()
            context['userprofile'] = profile

        elif user.is_executive:
            profile = user.get_executive_profile()
            context['userprofile'] = profile

        elif user.is_study_host:
            profile = user.get_study_host_profile()
            context['userprofile'] = profile

        elif user.is_active:
            #profile = user.get_user_profile()
            context['userprofile'] = self.request.user

        elif user.is_student and user.is_professor and user.is_executive:
            student_profile = user.get_student_profile()
            professor_profile = user.get_professor_profile()
            executive_profile = user.get_executive_profile()
            context['student_profile'] = student_profile
            context['professor_profile'] = professor_profile
            context['executive_profile'] = executive_profile
        return context


class AccountSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = forms.UserUpdateForm
    success_url = reverse_lazy('dashboard')
    context_object_name = 'preferences'

    def get_context_data(self, **kwargs):
        context = super(AccountSettingsUpdateView, self).get_context_data(**kwargs)

        user = self.request.user
        if user.is_student:
            profile = user.get_student_profile()
            context['userprofile'] = profile
        elif user.is_professor:
            profile = user.get_professor_profile()
            context['userprofile'] = profile
        elif user.is_executive:
            profile = user.get_executive_profile()
            context['userprofile'] = profile
        elif user.is_active:
            #profile = user.get_user_profile()
            context['userprofile'] = self.request.user
        return context

'''
class AccountProfilesView(LoginRequiredMixin, UpdateView):
    def get_context_data(self, **kwargs):
'''


class AccountProfilesView(LoginRequiredMixin, UpdateView):
    # All users can access this view
    model = get_user_model()
    #success_url = reverse_lazy('dashboard')
    template_name = 'accounts/profile_form.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(AccountProfilesView, self).get_context_data(**kwargs)
        user = self.request.user

        if not self.request.POST:
            if user.is_student:
                profile = user.get_student_profile()
                context['userprofile'] = profile
                context['form_student'] = forms.StudentProfileForm()
            if user.is_professor:
                profile = user.get_professor_profile()
                context['userprofile'] = profile
                context['form_professor'] = forms.ProfessorProfileForm()
                print ("profesor form is", context['form_professor'])
            if user.is_executive:
                profile = user.get_executive_profile()
                context['userprofile'] = profile
                context['form_executive'] = forms.ExecutiveProfileForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = super(AccountProfilesView, self).post(request, *args, **kwargs)
        user = self.request.user
        if self.request.method == 'POST':
            if user.is_student:
                context['form_student'] = forms.StudentProfileForm(
                    self.request.POST)
            elif user.is_professor:
                context['form_professor'] = forms.ProfessorProfileForm(
                    self.request.POST)
            elif user.is_executive:
                context['form_executive'] = forms.ExecutiveProfileForm(
                    self.request.POST)
        return context

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        user = self.request.user
        user = form.save()
        if user.is_student:
            student = context['form_student'].save(commit=False)
            student.user = user
            student.save()
        if user.is_professor:
            professor = context['form_professor'].save(commit=False)
            professor.user = user
            professor.save()
        if user.is_executive:
            executive = context['form_executive'].save(commit=False)
            executive.user = user
            executive.save()
        return super(AccountProfilesView, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')


