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