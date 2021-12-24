from django import forms
from PC_attend.models import PcAttendance


class CreateAttendanceForm(forms.ModelForm):
    class Meta:
        model = PcAttendance
        fields = ('pcs_name', 'pc_member', 'service_date', 'present', 'reason'

                  )
