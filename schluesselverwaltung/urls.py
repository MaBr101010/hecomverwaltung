__author__ = 'Braun'

from django.conf.urls import patterns, include, url, static

urlpatterns = patterns('',
    url(r'^all/$', 'schluesselverwaltung.views.mitarbeiter_all'),
    url(r'^get/(?P<persoNr>\d+)/$', 'schluesselverwaltung.views.mitarbeiter'),
    )