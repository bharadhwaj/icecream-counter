from django.db import models

from users.models import User


class Meeting(models.Model):
    name = models.CharField(max_length=255)
    absent_fee = models.PositiveIntegerField(default=50)
    camera_off_fee = models.PositiveIntegerField(default=25)
    host = models.ForeignKey(
        to=User, related_name="meetings", on_delete=models.CASCADE, null=False
    )
    participants = models.ManyToManyField(User, related_name="participants", blank=True)

    def __str__(self) -> str:
        return self.name


class DailyAttendance(models.Model):
    date = models.DateField()
    meeting = models.ForeignKey(
        to=Meeting, related_name="attendance", on_delete=models.CASCADE, null=False
    )
    absentees = models.ManyToManyField(to=User, related_name="absentees")
    camera_off_participants = models.ManyToManyField(
        to=User, related_name="camera_off_participants"
    )

    def __str__(self) -> str:
        return f" {self.meeting.name} - {self.date}"
