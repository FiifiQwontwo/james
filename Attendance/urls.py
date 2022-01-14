from django.urls import path
from .views import index, pcs_detail, create_pcs_name, list_pcs, create_name_pcs

app_name = 'Attendance'
urlpatterns = [
    path('', index, name='home page'),
    path('pcs/', list_pcs, name='list_pcs'),
    path('pcs/<slug:slug>', pcs_detail, name='pcadetails'),
    path('add/', create_pcs_name, name='add_new_pcs'),
    path('addpc/', create_name_pcs, name='add_pcs'),
]
