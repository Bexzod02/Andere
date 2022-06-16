from django.contrib import admin

from .models import GetInTouch, Subscribe
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject',)
    search_fields = ('name', 'email')

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')

admin.site.register(GetInTouch, ContactAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
