from django.urls import path

from PC_attend import views
from PC_attend.views import *

app_name = 'PC_attend'

urlpatterns = [
    path('Alist/', attendance_list, name='attendance_list'),
    # path('Alist/<slug:slug>', attendance_detail, name='details_attend'),
    path('Acreate/', views.CreateAttendanceView.as_view(), name='new_attend')


]
