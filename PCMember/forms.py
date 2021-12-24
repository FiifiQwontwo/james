from django import forms
from PCMember.models import PcMember


class CreateMemberForm(forms.ModelForm):
    class Meta:
        model = PcMember
        fields = ('pcs_name', 'pc_member_last_name',
                  'pc_member_first_name', 'pc_member_othername', 'whats_phone',
                  'pc_member_phone', 'pc_member_gps_address', 'pc_member_house_address'

                  )
