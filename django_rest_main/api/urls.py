from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()
router.register('employees',EmployeeViewset,basename='employee')
urlpatterns = [
    path('students/',studentView,name='studentview'),
    path('students/<int:pk>/',studentDetailView,name='studentDetailView'),
    # path('employees/',Employees.as_view(),name='Employees'),
    # path('employees/<int:pk>/',EmployeesDetailView.as_view(),name='EmployeesDetailView')
    path('',include(router.urls)),
    path('blogs/',BlogsView.as_view()),
    path('comments/',CommentsView.as_view()),
]
