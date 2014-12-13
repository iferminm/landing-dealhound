from django.conf.urls import patterns, include, url
from django.contrib import admin

from landing.views import LandingView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jagten_landing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^$', LandingView.as_view(), name='/'),
)
