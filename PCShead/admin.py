from django.contrib import admin
from . models import Pchead
# Register your models here.


@admin.register(Pchead)
class PcheadAdmin(admin.ModelAdmin):
    list_display = ("pcs_name", "pc_head_last_name", "pc_head_first_name", )
    search_fields = ['pcs_head', "pc_head_last_name"]
