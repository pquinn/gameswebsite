__author__ = 'phil'
from django.conf import settings # import the settings file
from datetime import datetime

def constants(context):
    # return the value you want as a dictionary. you may add multiple values in there.
    return {'TWITTER_URL': 'http://www.twitter.com/Phillmatic19',
            'FACEBOOK_URL': 'http://www.facebook.com/phillmatic19',
            'SOC_URL' : 'http://careers.stackoverflow.com/pquinn',
            }

def time(context):
    return {'current_time': datetime.now(),}

def current_site_url():
    """Returns fully qualified URL (no trailing slash) for the current site."""
    from django.contrib.sites.models import Site
    current_site = Site.objects.get_current()
    protocol = getattr(settings, 'MY_SITE_PROTOCOL', 'http')
    port     = getattr(settings, 'MY_SITE_PORT', '')
    url = '%s://%s' % (protocol, current_site.domain)
    if port:
        url += ':%s' % port
    return url

def django_root_url(fq=False):
    """Returns base URL (no trailing slash) for the current project.

    Setting fq parameter to a true value will prepend the base URL
    of the current site to create a fully qualified URL.

    The name django_root_url is used in favor of alternatives
    (such as project_url) because it corresponds to the mod_python
    PythonOption django.root setting used in Apache.
    """
    url = getattr(settings, 'MY_DJANGO_URL_PATH', '')
    if fq:
        url = current_site_url() + url
    return url

def urls(context):
    return {'CURRENT_URL': current_site_url(),
            'DJANGO_ROOT': django_root_url(),
            }