from django.urls import path
from .views import *
urlpatterns = [
    path('students/',studentView,name='studentview'),
    path('students/<int:pk>/',studentDetailView,name='studentDetailView'),
    path('employees/',Employees.as_view(),name='Employees'),
    path('employees/<int:pk>/',EmployeesDetailView.as_view(),name='EmployeesDetailView')

]
