from django.urls import path

from PC_attend import views
from PC_attend.views import *

app_name = 'PC_attend'

urlpatterns = [
    path('Alist/', attendance_list, name='attendance_list'),
    path('Alist/<id>', detail_view_attendance, name='details_attend'),
    path('Acreate/', attendance_add, name='new_attend'),
    path('ajax/load_member', load_members, name='ajax_load_member'),

]
