from django.db import models
from django.forms import ModelForm
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save


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
    is_public = models.BooleanField(default=False)
    # figure out how to deal with this
    #first_to_unlock = models.OneToOneField(Member, default=None)

    def __unicode__(self):
        return self.name

class Member(models.Model):
    tag = models.CharField(max_length=16)
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)
    nuid = models.CharField(max_length=10, primary_key=True)
    email = models.CharField(max_length=30, unique=True)
    achievements = models.ManyToManyField(Unlockable, through="Unlocked")
    score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.tag

    def has_achievement(self, achievement):
        return self.achievements.values

class Unlocked(models.Model):
    member = models.ForeignKey(Member)
    unlockable = models.ForeignKey(Unlockable)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode("{0:>s} unlocked \"{1:>s}\"".format(self.member.tag, self.unlockable.name))

class MemberForm(ModelForm):
    class Meta:
        model = Member

class PartialMemberForm(ModelForm):
    class Meta:
        model = Member
        exclude = ('achievements','score',)

class PartialUnlockableForm(ModelForm):
    class Meta:
        model = Unlockable
        exclude = ('is_public',)

@receiver(post_save, sender=Unlocked)
def update_scores(sender, **kwargs):
    if kwargs.get('created', False):
        members = Member.objects.all()
        for member in members:
            unlockables = member.achievements.all()
            member_total = 0
            for unlockable in unlockables:
                member_total += unlockable.point_value
            member.score = member_total
            member.save()

@receiver(post_save, sender=Unlockable)
def make_feat_public(sender, **kwargs):
    if kwargs.get('created', False):
        unlockable = kwargs.get('instance')
        if unlockable.type == 'feat':
            unlockable.is_public = True
            unlockable.save()

@receiver(post_save, sender=Unlocked)
def make_achievement_public(sender, **kwargs):
    if kwargs.get('created', False):
        unlocked = kwargs.get('instance')
        achievement = unlocked.unlockable
        if achievement.is_public == False:
            achievement.is_public = True
            achievement.save()

#this is being ran twice for some odd reason
#@receiver(post_save, sender=Member)
#def member_created(sender, **kwargs):
#    if kwargs.get('created', False):
#        member = kwargs.get('instance')
#        unlockable = get_object_or_404(Unlockable, name="Attend a meeting!")
#        unlocked = Unlocked(member=member, unlockable=unlockable)
#        unlocked.save()