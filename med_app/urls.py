from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
app_name = 'myapp'

urlpatterns = [

  
    path('', include(router.urls)),
   
 ]



 