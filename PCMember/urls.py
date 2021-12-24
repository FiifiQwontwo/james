from django.urls import path
from PCMember.views import create_pcmember, member_list, member_detail

app_name = 'PCMember'
urlpatterns = [
    path('list/', member_list, name='listmemeber'),
    path('list/<slug:slug>', member_detail, name='member details'),
    path('add/', create_pcmember, name='new member'),
]
