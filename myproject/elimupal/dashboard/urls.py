from django.urls import path
from . import views

urlpatterns = [
    path('dashboard1/', views.dashboard, name='dashboard1'),
    path('dashboard2/', views.dashboard2, name='dashboard2'),
    path('dashboard3/', views.dashboard3, name='dashboard3'),
]