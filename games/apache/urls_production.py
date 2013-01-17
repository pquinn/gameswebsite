from django.contrib import admin
from django.conf.urls.defaults import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('games.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
