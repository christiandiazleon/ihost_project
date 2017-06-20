from __future__ import unicode_literals
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from .models import LodgingOffer, StudiesOffert, RoomInformation

from host_information.models import LodgingServiceOffer


from .forms import (LodgingOfferForm,
    StudiesOffertForm, LodgingOfferSearchForm,)

from django.views.generic.edit import FormView
from haystack.query import SearchQuerySet

# Create your views here.

class LodgingOfferSearch(LoginRequiredMixin, FormView):
    template_name = 'hosts/lodgingoffer_search.html'

    # first we instantiate the SearchForm that we created before.
    form_class = LodgingOfferSearchForm()

    def get(self, request, *args, **kwargs):
        # We are going to submit the form using the GET method so that the
        # resulting URL includes the query parameter.
        form = LodgingOfferSearchForm(self.request.GET or None)
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(LodgingOfferSearch, self).get_context_data(**kwargs)
        user = self.request.user
        form = LodgingOfferSearchForm(self.request.GET or None)

        # When the form is submitted, we instantiate it with the submitted GET
        # data and we check that the given data is valid. If the form is
        # valid, we use the we use SearchQuerySet to perform a search for
        # indexed LodgingOffer objects whose main content contains the given
        # query
        if form.is_valid():
            cd = form.cleaned_data
            # The load_all() method loads all related LodgingOffer objects
            # from the database at once
            # With this method, we populate the search results with the
            # database objects to avoid per-object access to the database when
            # iterating over results to access object data.
            results = SearchQuerySet().models(LodgingOffer)\
                          .filter(content=cd['query']).load_all()

            # Finally, we store the total number of results in a total_results
            # variable and pass the local variables as context to render a
            # template.
            total_results = results.count()
            context.update({
                'cd': cd,
                'results':results,
                'total_results': total_results,
            })
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
        return context

def studies_offers_by_user(request, username):
    user = request.user
    studies_offers = StudiesOffert.objects.filter(created_by__username=username)

    if user.is_study_host:
        profile = user.get_study_host_profile()


    return render(
        request,
        'hosts/studiesoffer_list.html',
        {'studies_offers':studies_offers,
        'userprofile':profile}
    )

def lodging_offers_by_user(request, username):
    user = request.user
    lodging_offers = LodgingOffer.objects.filter(created_by__username=username)

    if user.is_hosting_host:
        profile = user.get_hosting_host_profile()


    return render(
        request,
        'hosts/lodgingoffer_list.html',
        {'lodging_offers':lodging_offers,
        'userprofile':profile}
    )

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
    #success_url = reverse_lazy('dashboard')

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


class HostingOfferUpdateView(LoginRequiredMixin, UpdateView):
    model = LodgingOffer
    form_class = LodgingOfferForm
    success_url = reverse_lazy("dashboard")
    # success_url = reverse_lazy("hosts:detail-lodging-offer")

    def get_context_data(self, **kwargs):
        context = super(HostingOfferUpdateView, self).get_context_data(**kwargs)

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
        return context


class HostingOfferDetailView(LoginRequiredMixin, DetailView):
    model=LodgingOffer
    template_name = 'lodgingoffer_detail.html'
    context_object_name = 'lodgingofferdetail'

    def get_context_data(self, **kwargs):
        context = super(HostingOfferDetailView, self).get_context_data(**kwargs)
        user = self.request.user


        roominformation = LodgingOffer.objects.get(pk=self.kwargs.get('pk'))
        room_information_lodging_offer = roominformation.room_information.all()
        #inf = self.kwargs['room_information_set.all()']

        #room_information = set(queryset.values_list('room_information__name', flat=True).distinct())

        context['lodgingoffer'] = room_information_lodging_offer

        #queryset2 = LodgingOffer.objects.filter(offered_services__lodgingserviceoffer=LodgingServiceOffer.objects.all())

        #offeredservices = set(queryset2.values_list('offered_services__name', flat=True).distinct())

        offeredservices = LodgingOffer.objects.get(pk=self.kwargs.get('pk'))

        query = offeredservices.offered_services.all()


        context['offeredservices'] = query


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
        return context


class StudyOfferCreateView(LoginRequiredMixin, CreateView):
    model = StudiesOffert
    form_class = StudiesOffertForm
    #success_url = reverse_lazy("host:detail")
    #success_url = reverse_lazy("dashboard")

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


class StudyOffertDetailView(LoginRequiredMixin, DetailView):
    model=StudiesOffert
    template_name = 'studyoffert_detail.html'
    context_object_name = 'studyofferdetail'

    def get_context_data(self, **kwargs):
        context = super(StudyOffertDetailView, self).get_context_data(**kwargs)
        user = self.request.user


        studiestype_query = StudiesOffert.objects.get(pk=self.kwargs.get('pk'))
        studies_type_study_offert = studiestype_query.studies_type_offered.all()
        context['studiestypeoffered'] = studies_type_study_offert


        scholarships_query = StudiesOffert.objects.get(pk=self.kwargs.get('pk'))
        scholarships = scholarships_query.scholarships.all()
        context['scholarships'] = scholarships


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
        return context


class StudyOfferUpdateView(LoginRequiredMixin, UpdateView):
    model = StudiesOffert
    form_class = StudiesOffertForm
    success_url = reverse_lazy("dashboard")
    # success_url = reverse_lazy("hosts:detail-lodging-offer")

    def get_context_data(self, **kwargs):
        context = super(StudyOfferUpdateView, self).get_context_data(**kwargs)

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
        return context
