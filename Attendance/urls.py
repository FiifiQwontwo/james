from django.urls import path
from .views import index, pcs_detail

urlpatterns = [
    path('', index, name='home page'),
    path('/<slug:slug>', pcs_detail, name='chapel head details'),

]
