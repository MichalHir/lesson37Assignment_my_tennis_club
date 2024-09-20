from django.urls import include, path

from courts import admin
from . import views

urlpatterns = [
    
    path('', views.members, name='members'),
    path('details/<int:id>', views.details, name='details'),
]

