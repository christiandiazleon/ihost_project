from django.conf.urls import url
from .views import HostingOfferCreateView

urlpatterns = [

    url(r'^lodging-host/offer/new',
        HostingOfferCreateView.as_view(),
        name='hosting-host'
    ),

    url(r'^lodging-host/offer/search',
        HostingOfferCreateView.as_view(),
        name='hosting-host-search'
    ),

]
