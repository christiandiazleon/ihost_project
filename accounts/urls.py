from __future__ import unicode_literals
from django.conf.urls import url
from . import views
from .forms import ProfessorProfileForm
from .models import ProfessorProfile, ExecutiveProfile


urlpatterns = [
    # url(r"login/", views.LoginView.as_view(), name="login"),
    url(r"logout/$", views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SignUpView.as_view(), name="signup"),
    url(r"join/$", views.signup, name="join"),


    #url(r"^preferences/(?P<pk>\d+)$",
    #    views.AccountSettingsUpdateView.as_view(),
    #    name='preferences'
    #),

    # basado en el usernames
    url(r"^profile/(?P<slug>[\w\-]+)/$",
        views.AccountProfilesView.as_view(),
            name='profile'
    ),

    url(r"^preferences/(?P<slug>[\w\-]+)/$",
        views.AccountSettingsUpdateView.as_view(),
        name='preferences'
    ),




]
