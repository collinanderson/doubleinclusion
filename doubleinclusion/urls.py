from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render

urlpatterns = [
    # Examples:
    # url(r'^$', 'doubleinclusion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', render, {'template_name': 'one.html'}),
]
