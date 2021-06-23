from django.contrib import admin

from .models import PersonalNote


class PersonalNoteAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(PersonalNote, PersonalNoteAdmin)
