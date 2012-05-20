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
    url(r'^join/$', 'direct_to_template', {'template': 'join.html'}),
    url(r'^about/$', 'direct_to_template', {'template': 'about.html'}),
    url(r'^events/$', 'direct_to_template', {'template': 'events.html'}),
    url(r'^contact/$', 'direct_to_template', {'template': 'contact.html'}),
    url(r'^projects/$', 'direct_to_template', {'template': 'projects.html'}),
    #change this to a non generic view, for the love of god
    url(r'^profile/$', 'direct_to_template', {'template': 'users/profile.html'}),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'users/login.html',
                              'redirect_field_name': 'next'}),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

urlpatterns += patterns('tracker.views',
    (r'^tracker/leaderboard/$', 'leaderboard'),
    (r'^tracker/member/add-member/$', 'add_member'),
    (r'^tracker/member/save-member/$', 'save_member'),
    (r'^tracker/unlockable/feat-list/$', 'list_feats'),
)

urlpatterns += patterns('tracker.views',
    (r'^tracker/unlockable/(?P<unlockable_id>\d+)/$', 'unlockable_detail')
)

urlpatterns += patterns('',
    # ... other URL defs and includes here ....
    (r'', include(auth_urls)),
)