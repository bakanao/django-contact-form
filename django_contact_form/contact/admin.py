from django.contrib import admin

from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'ip', 'location')
    search_fields = ['email']


admin.site.register(Contact, ContactAdmin)
