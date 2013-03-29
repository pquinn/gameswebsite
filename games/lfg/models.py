#LFG
from django.db import models

ROLE_CHOICES = (
    (u'DS', u'Designer'),
    (u'DV', u'Developer'),
    (u'AR', u'Artist'),
    (u'SD', u'Sound')
)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    role = models.CharField(max_length=4, choices=ROLE_CHOICES)
    time_per_week = models.IntegerField()
    skills = models.TextField()



