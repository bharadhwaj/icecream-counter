from django import forms

from .models import DailyAttendance


class DailyAttendancesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DailyAttendancesForm, self).__init__(*args, **kwargs)
        self.current_meeting = kwargs["instance"].meeting

    class Meta:
        model = DailyAttendance
        fields = ["id", "date", "meeting", "absentees", "camera_off_participants"]

    def clean(self):
        meeting = self.cleaned_data.get("meeting")
        absentees = self.cleaned_data.get("absentees")
        camera_off_participants = self.cleaned_data.get("camera_off_participants")
        non_participants = list(
            set(absentees | camera_off_participants) - set(meeting.participants.all())
        )
        if non_participants:
            if len(non_participants) == 1:
                raise forms.ValidationError(
                    f"{non_participants[0].username} is not a participant of this meeting."
                )
            else:
                non_participant_users = ", ".join(
                    non_participant.username for non_participant in non_participants
                )
                raise forms.ValidationError(
                    f"{non_participant_users} are not participants of this meeting."
                )
        return self.cleaned_data
