from django.conf import settings
from django.contrib import admin

from .forms import DailyAttendancesForm
from .models import Meeting, DailyAttendance


admin.site.site_header = settings.SITE_HEADER
admin.site.index_title = settings.INDEX_TITLE


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    search_fields = ["name", "host"]
    list_display = ("id", "name", "host")


@admin.register(DailyAttendance)
class DailyAttendanceAdmin(admin.ModelAdmin):
    search_fields = ["id", "meeting__name"]
    list_display = ("id", "date", "meeting")
    form = DailyAttendancesForm
    pass
