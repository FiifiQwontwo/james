from django.urls import path
from .views import index, pcs_detail, create_pcs_name, pcs_add, list_pcs

app_name = 'Attendance'
urlpatterns = [
    path('', index, name='home page'),
    path('pcs/', list_pcs, name='list_pcs'),
    path('pcs/<slug:slug>', pcs_detail, name='pcadetails'),
    path('new_pcs/', create_pcs_name, name='add_new_pcs'),
    path('pcsadd/', create_pcs_name, name='new_pcs'),
    path('addpc/', pcs_add, name='add_pcs'),
    ]

