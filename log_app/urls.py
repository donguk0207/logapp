from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_log/', views.generate_log_ajax, name='generate_log_ajax'),
    path('', views.logapp_index),
]
