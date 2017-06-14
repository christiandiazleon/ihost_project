from django.conf.urls import url
from .views import HostingOfferCreateView, HostingHostPageView, StudyHostPageView, StudyOfferCreateView

urlpatterns = [

    url(r'^lodging-host/offer/new',
        HostingOfferCreateView.as_view(),
        name='hosting-host'
    ),

    url(r'^lodging-host/offer/search',
        HostingOfferCreateView.as_view(),
        name='hosting-host-search'
    ),

    url(r'^be-a-hosting-host/',
        HostingHostPageView.as_view(),
        name='be-a-hosting-host'
    ),

    url(r'^be-a-study-host/',
        StudyHostPageView.as_view(),
        name='be-a-study-host'
    ),

    url(r'^studies-host/offer/new',
        StudyOfferCreateView.as_view(),
        name='study-host'
    ),



]
