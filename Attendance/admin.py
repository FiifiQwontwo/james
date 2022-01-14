from django.contrib import admin
from .models import PCS


# Register your models here.

@admin.register(PCS)
class PCSAdmin(admin.ModelAdmin):
    list_display = ("pcs_name",)
    search_fields = ('pcs_name',)
    prepopulated_fields = {'slug': ('pcs_name',)}


