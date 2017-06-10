"""ihost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from .views import  home_files, HomePageView
from accounts.views import DashboardProfileView


# Return a url pattern to serve the static files
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^accounts/', include('accounts.urls', namespace = 'accounts')),
    # conecta a vistas como logot signyp
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # para autorizacion

    #verdadero
    # url(r'^accounts/', include('django.contrib.auth.urls'), name='login'),

    # I don't assign namespace because this is django URL



    url(r'^$', HomePageView.as_view(), name='home'),

    url(r'^dashboard/', DashboardProfileView.as_view(), name='dashboard'),


    # which is a regular expression that takes the desired urls and passes as
    # an argument the filename, i.e. robots.txt or humans.txt.
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),

    url(r'^become-a-host/',
        include('hosts.urls', namespace='hosts')
    ),

]


# urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
