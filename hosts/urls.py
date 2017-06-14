from django.conf.urls import url
from .views import (HostingOfferCreateView, HostingOfferUpdateView, HostingHostPageView, StudyHostPageView, StudyOfferCreateView,
    HostingOfferDetailView, lodging_offers_by_user)


urlpatterns = [

    # Create Hosting Offer
    url(r'^lodging-offer/new',
        HostingOfferCreateView.as_view(),
        name='hosting-host'
    ),

    # List Hosting Offers
    url(r'^lodging-offers/by/(?P<username>[-\w]+)/',
        lodging_offers_by_user,
        name='list'
    ),


    # Edit Hosting offer
    url(r"^lodging-offer/(?P<slug>[\w.\-]+)/edit/$",
        HostingOfferUpdateView.as_view(),
        name='edit-lodging-offer'
    ),

    # Detail of a Hosting Offer
    url(r"^lodging-offer/(?P<slug>[\w.\-]+)/",
        HostingOfferDetailView.as_view(),
        name='detail'
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
    url(r'^studies-offer/new',
        StudyOfferCreateView.as_view(),
        name='study-host'
    ),



]
