from django.conf.urls import url
from .views import (HostingOfferCreateView, HostingOfferUpdateView, HostingHostPageView, StudyHostPageView, StudyOfferCreateView, StudyOffertDetailView, HostingOfferDetailView, lodging_offers_by_user, studies_offers_by_user, StudyOfferUpdateView, LodgingOfferSearch,
    StudiesOffertSearch, HostingOfferDeleteView, StudyOfferDeleteView, LodgingOffersByUser,)


urlpatterns = [

    # ----------------------Hosting Offers-------------------

    # Create Hosting Offer
    url(r'^lodging-offer/new/$',
        HostingOfferCreateView.as_view(),
        name='hosting-host'
    ),

    # List Hosting Offers
    url(r'^lodging-offers/by/u/@(?P<username>[-\w]+)/$',
        lodging_offers_by_user,
        name='list'
    ),


    url(r'^ofertas/by/u/@(?P<username>[-\w]+)/$',
       LodgingOffersByUser.as_view(),
        name='list2'
    ),


    # Edit Hosting offer
    url(r"^lodging-offer/(?P<pk>\d+)/edit/$",
        HostingOfferUpdateView.as_view(),
        name='edit-lodging-offer'
    ),

    # Delete of a Hosting Offer
    url(r"^lodging-offer/(?P<pk>\d+)/delete/$",
        HostingOfferDeleteView.as_view(),
        name='delete-lodging-offer'
    ),

    # Detail a Hosting Offer
    url(r"^lodging-offer/(?P<pk>\d+)/$",
        HostingOfferDetailView.as_view(),
        name='detail'
    ),




    # Search Hosting Offer
    url(r'^lodging-offer/search/$',
        LodgingOfferSearch.as_view(),
        name='hostingoffer-search'
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
    url(r'^studies-offers/by/u/@(?P<username>[-\w]+)/',
        studies_offers_by_user,
        name='studiesofferlist'
    ),

    # Edit Studies offer
    url(r"^study-offer/(?P<pk>\d+)/edit/",
        StudyOfferUpdateView.as_view(),
        name='edit-study-offer'
    ),



    # Delete of a Hosting Offer
    url(r"^study-offer/(?P<pk>\d+)/delete/$",
        StudyOfferDeleteView.as_view(),
        name='delete-study-offer'
    ),

    #Detail of Studies Offert
    url(r'^study-offer/(?P<pk>\d+)/',
        StudyOffertDetailView.as_view(),
        name='studyoffertdetail'
    ),

    # Search Studies Offer
    url(r'^study-offer/search/$',
        StudiesOffertSearch.as_view(),
        name='studyoffer-search'
    ),





]
