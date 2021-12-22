from django.contrib import admin
from . models import PcMember
# Register your models here.


@admin.register(PcMember)
class PcMemberAdmin(admin.ModelAdmin):
    list_display = ("pcs_name", "pcs_head", "pc_member_last_name", "pc_member_first_name", )
    search_fields = ['pcs_head', "pc_member_last_name"]
