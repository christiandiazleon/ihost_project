from django.conf.urls import url
from .views import (HostingOfferCreateView, HostingOfferUpdateView, HostingHostPageView, StudyHostPageView, StudyOfferCreateView, StudyOffertDetailView, HostingOfferDetailView, lodging_offers_by_user, studies_offers_by_user, StudyOfferUpdateView)


urlpatterns = [

    # ----------------------Hosting Offers-------------------

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
    url(r"^lodging-offer/(?P<pk>\d+)/edit/",
        HostingOfferUpdateView.as_view(),
        name='edit-lodging-offer'
    ),

    # Detail of a Hosting Offer
    url(r"^lodging-offer/(?P<pk>\d+)/",
        HostingOfferDetailView.as_view(),
        name='detail'
    ),


    # Search Hosting Offer
    url(r'^lodging-host/offer/search',
        HostingOfferCreateView.as_view(),
        name='hosting-host-search'
    ),


    # ----------------------Template Views-------------------
    url(r'^be-a-hosting-host/',
        HostingHostPageView.as_view(),
        name='be-a-hosting-host'
    ),

    url(r'^be-a-study-host/',
        StudyHostPageView.as_view(),
        name='be-a-study-host'
    ),

    # ----------------------Study Offers-------------------

    # Create Study Host Offer
    url(r'^studies-offer/new',
        StudyOfferCreateView.as_view(),
        name='study-host'
    ),

    # List Study Host Offers
    url(r'^studies-offers/by/(?P<username>[-\w]+)/',
        studies_offers_by_user,
        name='studiesofferlist'
    ),

    # Edit Studies offer
    url(r"^study-offer/(?P<pk>\d+)/edit/",
        StudyOfferUpdateView.as_view(),
        name='edit-study-offer'
    ),


    #Detail of Studies Offert
    url(r'^study-offer/(?P<pk>\d+)/',
        StudyOffertDetailView.as_view(),
        name='studyoffertdetail'
    ),





]
