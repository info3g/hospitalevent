from django.contrib import admin
from .models import Event_Management

from .models import EventSelect
from django.utils.html import format_html


admin.site.index_title = "Welcome to Event Admin Section"
admin.site.site_header="Events Dashboard"



class BookAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_cateogary', 'date', 'time', 'description', 'image', 'user_actions')
    def user_actions(self, obj):
        # TODO: Render action buttons
        print ('hhhhhhh : ', obj.pk)
        return format_html(
            '<a class="button" href="/crud/event_list_admin/?q={}">Users List</a>&nbsp;'.format(obj.pk),

        )


class EventSelectAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'event_id', 'message', 'created_at', 'updated_at')


admin.site.register(Event_Management, BookAdmin)
admin.site.register(EventSelect, EventSelectAdmin)

