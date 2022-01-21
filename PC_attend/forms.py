from django import forms
from PC_attend.models import PcAttendance
from PCMember.models import PcMember


class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, pc_member):
        """ Customises the labels for checkboxes"""
        return "%s" % pc_member.last_name


class CreateAttendanceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(CreateAttendanceForm, self).__init__(*args, **kwargs)
        self.fields['pc_member'].queryset = PcMember.objects.filter(
            user=self.request.user)

    class Meta:
        model = PcAttendance
        fields = ['pcs_name', 'pc_member', 'service_date', 'present', 'reason']

    service_date = forms.DateInput()
    pc_member = forms.ModelMultipleChoiceField(
        queryset=PcMember.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
