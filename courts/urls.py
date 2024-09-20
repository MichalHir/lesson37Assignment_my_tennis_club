from django.urls import path
from . import views

urlpatterns = [
    path('', views.courts, name='courts'),
    path('reserve/<int:id>', views.reserve, name='reserve'),
    path('release/<int:id>', views.release, name='release'),

]
