from django.contrib import admin
from django.conf.urls.defaults import *
from games import settings
from django.contrib.auth import urls as auth_urls
from tracker import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template': 'index.html'}),
    url(r'^events$', 'direct_to_template', {'template': 'events.html'}),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html',
                              'redirect_field_name': 'next'}),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

urlpatterns += patterns('tracker.views',
    (r'^tracker/members/add-member$', 'add_member'),
    (r'^tracker/members/save-member$', 'save_member'),
)

urlpatterns += patterns('',
    # ... other URL defs and includes here ....
    (r'', include(auth_urls)),
)