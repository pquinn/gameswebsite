__author__ = 'phil'
from tracker.models import Member, Unlockable, Unlocked
from django.contrib import admin

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['tag', 'nuid', 'email', 'year']}),
    ]
    list_display = ('nuid', 'tag', 'email', 'year')
    search_fields = ['tag', 'nuid', 'email', 'year']

admin.site.register(Member, MemberAdmin)
admin.site.register(Unlockable)
admin.site.register(Unlocked)
  