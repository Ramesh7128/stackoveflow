from django.conf.urls import patterns, include, url
from django.contrib import admin
from stackapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stackdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
)
