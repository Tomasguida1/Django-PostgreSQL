from django.urls import path
from .views import lists_vg, create_vg

urlpatterns =  [
    path('',lists_vg),
    path('new/',create_vg)
]