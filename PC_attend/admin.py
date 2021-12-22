from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(PcAttendance)
class PcAttendanceAdmin(admin.ModelAdmin):
    list_display = ("pcs_name", "pcs_head", "pc_member", "service_date", "present", "reason")
    search_fields = ['pcs_head',]
