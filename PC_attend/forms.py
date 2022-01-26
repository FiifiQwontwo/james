# from django.contrib.auth.models import User
from django import forms

import accounts.models
from PC_attend.models import PcAttendance
from PCMember.models import PcMember


class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, pc_member):
        """ Customises the labels for checkboxes"""
        return "%s" % pc_member.last_name


class CreateAttendanceForm(forms.ModelForm):
    class Meta:
        model = PcAttendance
        fields = ['pcs_name', 'pc_member', 'user', 'service_date', 'present', 'reason']

    service_date = forms.DateInput()
    pc_member = forms.ModelMultipleChoiceField(
        queryset=PcMember.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
