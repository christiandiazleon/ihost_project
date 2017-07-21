from django.conf.urls import url
from .views import ResearchGroupCreateView


urlpatterns = [
    url(r'^research-group/new',
            ResearchGroupCreateView.as_view(),
            name='research-group'
    ),
]
