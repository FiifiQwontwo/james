from django import forms
from PC_attend.models import PcAttendance
from PCMember.models import PcMember


class CreateAttendanceForm(forms.ModelForm):
    class Meta:
        model = PcAttendance
        fields = ['pcs_name', 'pc_member', 'service_date', 'present', 'reason']

    service_date = forms.DateInput()
    pc_member = forms.ModelMultipleChoiceField(
        queryset=PcMember.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


