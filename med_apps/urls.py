from django.urls import path, include
from rest_framework import routers
from .homiy.views import Homiy_arizasi
from .talaba.views import Talaba_qushish_view
router = routers.DefaultRouter()
app_name = 'myapp'

urlpatterns = [

  
    path('', include(router.urls)),
    path('ariza/',Homiy_arizasi.as_view({'get': 'list'}), name='ariza'),
    path('talaba_add/',Talaba_qushish_view.as_view(), name='talaba_add')
   
 ]



 