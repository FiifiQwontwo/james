from django import forms
from Attendance.models import PCS


class CreatePCSFOrm(forms.ModelForm):
    class Meta:
        model = PCS
        fields = ('pcs_name',

                  )
