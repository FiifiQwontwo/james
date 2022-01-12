from django import forms
from Attendance.models import PCS


class CreatePCSForm(forms.ModelForm):
    class Meta:
        model = PCS
        fields = ('pcs_name',

                  )
