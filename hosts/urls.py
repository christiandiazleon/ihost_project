from django.conf.urls import url
from .views import HostingOfferCreateView, HostingOfferUpdateView, HostingHostPageView, StudyHostPageView, StudyOfferCreateView

urlpatterns = [

    # Create Hosting Host Offer
    url(r'^lodging-host/offer/new',
        HostingOfferCreateView.as_view(),
        name='hosting-host'
    ),


    # Edit Hosting Host offer
    url(r"^lodging-host/offer/(?P<slug>[\w.\-]+)/$",
        HostingOfferUpdateView.as_view(),
        name='edit-lodging-offer'
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

    # Create Study Host Offer
    url(r'^studies-host/offer/new',
        StudyOfferCreateView.as_view(),
        name='study-host'
    ),



]
