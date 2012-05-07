from django.contrib import admin
from django.conf.urls.defaults import *
from games import settings
from django.contrib.auth import urls as auth_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template': 'index.html'}),
    url(r'^events$', 'direct_to_template', {'template': 'events.html'}),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html',
                                                        'redirect_field_name': 'next'}),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

urlpatterns += patterns('',
    # ... other URL defs and includes here ....
    (r'', include(auth_urls)),
)