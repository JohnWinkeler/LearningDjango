"""
Definition of urls for BasicProject2.
"""

from django.conf.urls import include, url
import MyApp1.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', BasicProject2.views.home, name='home'),
    # url(r'^BasicProject2/', include('BasicProject2.BasicProject2.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MyApp1.views.index, name='index'),
    url(r'^home$', MyApp1.views.index, name='home'),
    url(r'^about$', MyApp1.views.about, name='about'),
]
