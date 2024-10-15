from django.contrib import admin

from logs.models import Log


class LogAdmin(admin.ModelAdmin):
    fields = ["level", "message", "timestamp"]
    readonly_fields = ["timestamp"]
    list_display = ["level", "message", "timestamp"]


admin.site.register(Log, LogAdmin)
