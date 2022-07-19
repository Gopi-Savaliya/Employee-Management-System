from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_employee/', views.add_employee),
    path('remove_employee/', views.remove_employee),
    path('remove_employee/<int:emp_id>', views.remove_employee),
    path('filter_employee/', views.filter_employee)
]
