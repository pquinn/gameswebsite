__author__ = 'phil'
from games.lfg.models import Person
from django.contrib import admin

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['first_name', 'last_name', 'email', 'role', 'time_per_week', 'skills']}),
    ]
    list_display = ('first_name', 'last_name', 'email', 'role', 'time_per_week', 'skills')
    search_fields = ['first_name', 'last_name', 'email', 'role', 'time_per_week', 'skills']

admin.site.register(Person, PersonAdmin)
  