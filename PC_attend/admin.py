from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(PcAttendance)
class PcAttendanceAdmin(admin.ModelAdmin):
    list_display = ("get_members",  "service_date", "present", "pcs_name")
    search_fields = ['pcs_name', ]
