from __future__ import unicode_literals
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import LodgingOffer
from .forms import LodgingOfferForm, HostingOfferSearchForm
from django.views.generic.edit import FormView
from haystack.query import SearchQuerySet

# Create your views here.

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
