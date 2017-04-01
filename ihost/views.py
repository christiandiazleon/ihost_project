# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# where we have used the shortcut render, which lets you load a template,
# create a context adding a bunch of variables by default, such as information
# about the current logged-in user, or the current language, render it and
# return an HttpResponse, all in one function.
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = 'ihost/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # messages.info(self.request, 'hello http://example.com')
        user = self.request.user
        if user.is_authenticated():
            if user.is_student:
                profile = user.get_student_profile
                context['userprofile'] = profile
            elif user.is_professor:
                profile = user.get_professor_profile
                context['userprofile'] = profile
            elif user.is_executive:
                profile = user.get_executive_profile
                context['userprofile'] = profile
        return context

'''
def home(request):
    return render(request, "ihost/home.html")
'''


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
