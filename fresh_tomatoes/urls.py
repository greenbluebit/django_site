__author__ = 'Theodor'

from django.conf.urls import patterns, url

import views
#patterns to be recognized by web app
urlpatterns = patterns('',
    # ex: /fresh_tomatoes/
    url(r'^$', views.index, name='index'),
    # ex: /fresh_tomatoes/5/
    url(r'^(?P<movie_id>\d+)/$', views.detail, name='detail'),
    # ex: /fresh_tomatoes/search/value
    url(r'^search/([A-Za-z]+)', views.search, name="index"),
    url(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': 'django_site/staticfiles'}),
)