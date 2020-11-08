from django.contrib import admin

from .forms import DailyAttendancesForm
from .models import Meeting, DailyAttendance


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
