from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # web application end point
   path('students/',include('students.urls')),
    #  API endpoint  
    path('api/v1/',include('api.urls'))
]
