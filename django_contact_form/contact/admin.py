from django.contrib import admin

from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)


admin.site.register(Contact, ContactAdmin)
