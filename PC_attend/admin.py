from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(PcAttendance)
class PcAttendanceAdmin(admin.ModelAdmin):
    list_display = ("pcs_name", "pc_member", "service_date", "present", "reason")
    search_fields = ['pcs_name', ]
