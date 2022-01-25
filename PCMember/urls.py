from django.urls import path
from PCMember.views import create_pcmember, member_list, member_detail, Import_csv, create_mem, create_view_member

app_name = 'PCMember'
urlpatterns = [
    path('list_member/', member_list, name='listmemeber'),
    path('list_member/<slug:slug>', member_detail, name='member_details'),
    path('add_member/', create_pcmember, name='new_member'),
    path('import_csv_member/', Import_csv, name="Import_csv"),
    path('new_member/', create_mem, name='member_new'),
    path('mems_new', create_view_member),
]
