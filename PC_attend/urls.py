from django.urls import path
from PC_attend.views import attendance_list, attendance_detail, create_attendance

app_name = 'PC_attend'

urlpatterns = [
    path('list/', attendance_list, name='attendance list'),
    path('list/<slug:slug>', attendance_detail, name='details_attend'),
    path('create/', create_attendance, name='new attend')
]
