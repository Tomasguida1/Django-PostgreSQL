from django.urls import path
from .views import lists_vg

urlpatterns =  [
    path('',lists_vg)
]