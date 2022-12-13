from rest_framework import routers
from django.urls import path, include
from .homiy.views import Homiy_arizasi, Homiy_all_data_for_filtering
from .talaba.views import Talaba_qushish_view
router = routers.DefaultRouter()
app_name = 'myapp'


router.register('ariza',Homiy_arizasi,basename='ariza')
router.register('talaba',Talaba_qushish_view,basename='talaba')
router.register('homiy_all_data',Homiy_all_data_for_filtering,basename='homiy_all_data')

urlpatterns = [
    path('ariza/<pk>/',Homiy_arizasi.as_view({'get': 'retrieve'}),name='ariza-detail'),
    path('talaba/<pk>/',Homiy_arizasi.as_view({'get': 'retrieve'}),name='talaba-detail')

]


urlpatterns = router.urls


