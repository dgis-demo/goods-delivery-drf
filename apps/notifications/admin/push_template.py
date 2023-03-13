from django.contrib import admin

from apps.notifications.models import PushTemplate


@admin.register(PushTemplate)
class PushTemplateAdmin(admin.ModelAdmin):
    list_display = ['name']
