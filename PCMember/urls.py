from django.urls import path
from PCMember.views import  member_list, member_detail, Import_csv, member_add

app_name = 'PCMember'
urlpatterns = [
    path('list_member/', member_list, name='listmemeber'),
    path('list_member/<slug:slug>', member_detail, name='member_details'),
    # path('add_member/', create_pcmember, name='new_member'),
    path('import_csv_member/', Import_csv, name="Import_csv"),
    path('add_member/', member_add, name='member_new'),

]
