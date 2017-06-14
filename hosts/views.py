from __future__ import unicode_literals
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from .models import LodgingOffer, StudiesOffert


from .forms import LodgingOfferForm, HostingOfferSearchForm, StudiesOffertForm
from django.views.generic.edit import FormView
from haystack.query import SearchQuerySet

# Create your views here.


class StudyHostPageView(TemplateView):
    template_name = 'hosts/study_host_home.html'

    def get_context_data(self, **kwargs):
        context = super(StudyHostPageView, self).get_context_data(**kwargs)
        # messages.info(self.request, 'hello http://example.com')
        user = self.request.user
        if user.is_authenticated():
            if user.is_study_host:
                profile = user.get_study_host_profile
                context['userprofile'] = profile
        return context

class HostingHostPageView(TemplateView):
    template_name = 'hosts/hosting_host_home.html'

    def get_context_data(self, **kwargs):
        context = super(HostingHostPageView, self).get_context_data(**kwargs)
        # messages.info(self.request, 'hello http://example.com')
        user = self.request.user
        if user.is_authenticated():
            if user.is_hosting_host:
                profile = user.get_hosting_host_profile
                context['userprofile'] = profile
        return context

'''
class HostingOfferSearch(LoginRequiredMixin, FormView):
    template_name = 'hosts/search.html'
    form_class = HostingOfferSearchForm()

    def get(self, request, *args, **kwargs):
        form = HostingOfferSearchForm(self.request.GET or None)
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(HostingOfferSearch, self).get_context_data(**kwargs)
        user = self.request.user
        form = HostingOfferSearchForm(self.request.GET or None)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(LodgingOffer).filter(content=cd['query']).load_all()
'''

class HostingOfferCreateView(LoginRequiredMixin, CreateView):
    model = LodgingOffer
    form_class = LodgingOfferForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.created_by = self.request.user
        form.save()
        return super(HostingOfferCreateView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(HostingOfferCreateView, self).get_context_data(**kwargs)
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
        return context


class StudyOfferCreateView(LoginRequiredMixin, CreateView):
    model = StudiesOffert
    form_class = StudiesOffertForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.created_by = self.request.user
        form.save()
        return super(StudyOfferCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(StudyOfferCreateView, self).get_context_data(**kwargs)
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
        return context
