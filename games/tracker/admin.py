__author__ = 'phil'
from tracker.models import Member, Unlockable, Unlocked
from django.contrib import admin

admin.site.register(Member)
admin.site.register(Unlockable)
admin.site.register(Unlocked)
  