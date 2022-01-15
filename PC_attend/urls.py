from django.urls import path
from PC_attend.views import attendance_list, attendance_detail, create_attendance

app_name = 'PC_attend'

urlpatterns = [
    path('Alist/', attendance_list, name='attendance_list'),
    path('Alist/<slug:slug>', attendance_detail, name='details_attend'),
    path('Acreate/', create_attendance, name='new_attend')
]
