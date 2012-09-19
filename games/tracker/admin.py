__author__ = 'phil'
from tracker.models import Member, Unlockable, Unlocked
from django.contrib import admin

class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['tag', 'nuid', 'email', 'year', 'score']}),
    ]
    list_display = ('nuid', 'tag', 'email', 'year', 'score')
    search_fields = ['tag', 'nuid', 'email', 'year', 'score']

class UnlockableAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['type', 'name', 'description', 'point_value', 'is_public']}),
    ]
    list_display = ('type', 'name', 'point_value', 'is_public')
    search_fields = ['type', 'name', 'point_value', 'description']

class UnlockedAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['member', 'unlockable']}),
    ]
    list_display = ('member', 'unlockable', 'date')
    search_fields = ['member', 'unlockable', 'date']

admin.site.register(Member, MemberAdmin)
admin.site.register(Unlockable, UnlockableAdmin)
admin.site.register(Unlocked, UnlockedAdmin)
  