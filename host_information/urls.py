from django.conf.urls import url
from .views import ScholarshipCreateView, ResearchGroupCreateView


urlpatterns = [

    url(r'^scholarship/new',
            ScholarshipCreateView.as_view(),
            name='scholarship'
    ),

    url(r'^research-group/new',
            ResearchGroupCreateView.as_view(),
            name='research-group'
    ),


]
