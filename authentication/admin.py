

from django.contrib import admin
from.models import UserProfile, HardWareForm_table, Event, EventMember
from authentication.models import Event, EventMember
admin.site.register(UserProfile)
# Register your models here.
admin.site.register(HardWareForm_table)

class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['event', 'user']

admin.site.register(Event)
admin.site.register(EventMember, EventMemberAdmin)



