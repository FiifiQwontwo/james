from django.urls import path
from .views import index, pcs_detail, create_pcs_name, list_pcs

app_name = 'Attendance'
urlpatterns = [
    path('', index, name='home page'),
    path('pcs/', list_pcs, name='list_pcs'),
    path('pcs/<slug:slug>', pcs_detail, name='chapel head details'),
    path('new_pcs/', create_pcs_name, name='add new pcs'),

]
