"""
Definition of urls for Loteria.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^index/$',app.views.landingPage, name='landingPage'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^api/currentState$', app.views.currentLotteryState, name='apiGet'),
    url(r'^buy$', app.views.nakupTikety, name='buy'),
    url(r'^api/podajTiket$',app.views.podajTiket,name='podajTiket'),
    url(r'^api/pocetTiketov$',app.views.pocetTiketov,name='pocetTiketov'),
    url(r'^kupujem$',app.views.kupujem,name='kupujem'),
    url(r'^podanie$', app.views.podajTiket, name='podaj'),
    url(r'^zrebovanie$', app.views.zrebovanie, name='zrebovanie'),
    url(r'^historiaZrebovani$', app.views.historiaZrebovani, name='historiaZrebovani'),

    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]

from app.loteria import startup
startup()
