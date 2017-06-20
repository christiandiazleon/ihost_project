from __future__ import unicode_literals
from django.conf.urls import url, include
from django.conf import settings
from . import views
from .forms import ProfessorProfileForm
from .models import ProfessorProfile, ExecutiveProfile
from django.contrib.auth import views as auth_views

# app_name = 'accounts'

urlpatterns = [
    # url(r"login/", views.LoginView.as_view(), name="login"),

    # prueba de curso 1.11.
    #url(r"login/$", auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    #url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),

    # verdadero
    url(r"logout/$", views.LogoutView.as_view(), name="logout"),

    url(r"signup/$", views.SignUpView.as_view(), name="signup"),
    url(r"join/$", views.signup, name="join"),

    #url(r"^preferences/(?P<pk>\d+)$",
    #    views.AccountSettingsUpdateView.as_view(),
    #    name='preferences'
    #),

    # basado en el usernames
    #url(r"^profile/(?P<slug>[\w\-]+)/$",
    #    views.AccountProfilesView.as_view(),
    #        name='profile'
    #),

    url(r"^profile/(?P<slug>[\w\-]+)/$",
        views.user_profile_update_view,
            name='profile'
    ),

    url(r"^preferences/(?P<slug>[\w.\-]+)/$",
        views.AccountSettingsUpdateView.as_view(),
        name='preferences'
    ),


    #url(r"^preferences/(?P<slug>[\w.\-]+)/$",
    #   views.AccountSettingsUpdateView.as_view(),
    #    name='preferences'
    #),


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
