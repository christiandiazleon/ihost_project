from __future__ import unicode_literals

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
# form that handles authenticating the user
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect



from django.shortcuts import render, get_object_or_404
from django.conf import settings

#from . import forms
from .forms import (
    StudentProfileForm, ExecutiveProfileForm, ProfessorProfileForm, UserCreateForm, UserUpdateForm, StudyHostProfileForm, HostingHostProfileForm, UserEnterpriseUpdateForm,)
from .models import StudentProfile, ProfessorProfile, ExecutiveProfile, User

# Create your views here.

# Do not use at moment

'''

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
'''


class LogoutView(generic.RedirectView):
    # Redirect back to article list
    url = reverse_lazy('article_list')

    # se dispara cuando entra el request entrante
    def get(self, request, *args, **kwargs):
        # Llamamos a logout with the request
        logout(request)
        return super().get(request, *args, **kwargs)


class SignUpView(generic.CreateView):
    form_class = UserCreateForm
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


class DashboardProfileView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardProfileView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated():
            context['userprofile'] = user.profile

        '''
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

        elif user.is_hosting_host:
            profile = user.get_hosting_host_profile()
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
        '''
        return context


class AccountSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    success_url = reverse_lazy('dashboard')
    #context_object_name = 'preferences'

    '''
    def post(self, request, *args,**kwargs):
        form = self.get_form()
        if request.method=='POST':
            form = UserUpdateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return super(AccountSettingsUpdateView, self).form_valid(form)
        else:
            return super(AccountSettingsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        if self.request.method == 'POST':
            form = UserUpdateForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                form.save()
                return super(AccountSettingsUpdateView, self).form_valid(form)
        else:
            return super(AccountSettingsUpdateView, self).form_invalid(form)
        #return render(self.request, 'user_form.html', {'form':form})
    '''

    def get_context_data(self, **kwargs):
        context = super(AccountSettingsUpdateView, self).get_context_data(**kwargs)

        user = self.request.user
        context['userprofile'] = user.profile

        # To UserDetailView
        #speaklanguages = User.objects.get(pk=self.kwargs.get('pk'))
        #speak_languages_user = speaklanguages.speak_languages.all()
        #context['speaklanguages'] = speak_languages_user
        # print(speak_languages_user)

        '''
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
        elif user.is_hosting_host:
            profile = user.get_hosting_host_profile()
            context['userprofile'] = profile
        elif user.is_active:
            #profile = user.get_user_profile()
            context['userprofile'] = self.request.user
        '''
        return context

class AccountSettingsEnterpriseUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserEnterpriseUpdateForm
    success_url = reverse_lazy('dashboard')
    context_object_name = 'preferences'

    def get_context_data(self, **kwargs):
        context = super(AccountSettingsEnterpriseUpdateView, self).get_context_data(**kwargs)
        user = self.request.user
        context['userprofile'] = user.profile
        return context

@login_required
def user_profile_update_view(request, slug):
    user = request.user

    # Populate the forms and Instances (if applicable)
    form_profiles = []
    profile = user.profile

    if user.is_student:
        profile = user.get_student_profile()
        form_profiles.append({'form': StudentProfileForm,
                              'instance': user.studentprofile,
                              'title':"Student Details"
                            })
    if user.is_professor:
        profile = user.get_professor_profile()
        form_profiles.append({'form': ProfessorProfileForm, 'instance': user.professorprofile, 'title': "Professor Details"})

    if user.is_executive:
        profile = user.get_executive_profile()
        form_profiles.append({'form': ExecutiveProfileForm, 'instance': user.executiveprofile, 'title': "Executive Details"})

    if user.is_study_host:
        profile = user.get_study_host_profile()
        form_profiles.append({'form': StudyHostProfileForm, 'instance': user.studyhostprofile, 'title': "Study Host Details"})

    if user.is_hosting_host:
        profile = user.get_hosting_host_profile()
        form_profiles.append({'form': HostingHostProfileForm, 'instance': user.hostinghostprofile, 'title': "Hosting Host Details"})

    if request.method == 'POST':
        forms = [x['form'](data=request.POST, instance=x['instance'],) for x in form_profiles]
        if all([form.is_valid() for form in forms]):
            for form in forms:
                form.save()
            return redirect('dashboard')
    else:
        forms = [x['form'](instance=x['instance']) for x in form_profiles]

    return render(request, 'accounts/profile_form.html', {'forms': forms, 'userprofile':profile,})


'''
class AccountProfilesView(LoginRequiredMixin, UpdateView):
    # All users can access this view
    model = get_user_model()
    success_url = reverse_lazy('dashboard')
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
                # print ("profesor form is", context['form_professor'])
            if user.is_executive:
                profile = user.get_executive_profile()
                context['userprofile'] = profile
                context['form_executive'] = forms.ExecutiveProfileForm()
        else:
            if user.is_student:
                context['form_student'] = forms.StudentProfileForm(
                self.request.POST)
            if user.is_professor:
                context['form_professor'] = forms.ProfessorProfileForm(
                self.request.POST)
            if user.is_executive:
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
'''




'''
@login_required
def account_profiles__update_view(request, slug):
    user = request.user
    # user = get_object_or_404(User, username = slug)
    # user = User.objects.get(username = slug)
    # empty list
    _forms = []
    if user.is_student:
        profile = user.get_student_profile()
        _forms.append(forms.StudentProfileForm)
    if user.is_professor:
        profile = user.get_professor_profile()
        _forms.append(forms.ProfessorProfileForm)
    if user.is_executive:
        profile = user.get_executive_profile()
        _forms.append(forms.ExecutiveProfileForm)

    # user = get_object_or_404(settings.AUTH_USER_MODEL, username = slug)

    if request.method == 'POST':
        # Create a list with all formularies in which there is some POST
        # operation. This mean if there is one, two or three profiles together
        # or individual
        formularios =[Form(data = request.POST,instance=profile) for Form in _forms]

        if all([form.is_valid() for form in formularios]):
            # Only save dato to database if all formularies that send
            # the user in their request are correct or well formed in their
            # data. Check that all formularies has been filled
            for form in formularios:
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
            return redirect('dashboard')
    else:
        formularios = [Form() for Form in _forms]

    # Access to class Forms instanced (StudentProfileForm,
    # ProfessorProfileForm, ExecutiveProfileForm), through the __class__
    # pŕoperty which return the class onlying. An this class have another
    # property named __name__ which return the name of string of a class,
    # which is the same name with I did name the form classes
    # (StudentProfileForm, ProfessorProfileForm, ExecutiveProfileForm)
    # Next I call to their string method to grant that I always will return
    # a string and I call to lower.

    # The idea with this is place data into a python dictionarie and access
    # to it
    data = {form.__class__.__name__.__str__().lower(): form for form in formularios}
    data['userprofile'] = profile
    return render(request, 'accounts/profile_form.html', data,)
'''
