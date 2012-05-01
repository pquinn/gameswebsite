from django.db import models

YEAR_CHOICES = (
    (u'FR', u'Freshman'),
    (u'SO', u'Sophomore'),
    (u'MI', u'Middler'),
    (u'JR', u'Junior'),
    (u'SR', u'Senior')
)

UNLOCKABLE_TYPE_CHOICES = (
    (u'ach', u'Achievement'),
    (u'feat', u'Feat')
)

class Unlockable(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    point_value = models.IntegerField()
    type = models.CharField(max_length=4, choices=UNLOCKABLE_TYPE_CHOICES)

class Member(models.Model):
    tag = models.CharField(max_length=16)
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)
    nuid = models.CharField(max_length=10, primary_key=True)
    email = models.CharField(max_length=30, unique=True)
    achievements = models.ManyToManyField(Unlockable, through="Unlocked")

class Unlocked(models.Model):
    member = models.ForeignKey(Member)
    unlockable = models.ForeignKey(Unlockable)
    date = models.DateTimeField(auto_now_add=True)