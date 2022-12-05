from django.urls import path, include
from .views import ArizaRuyhat, HomiyDetailView,TalabaDetailView, TalabaQushishView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ariza', ArizaRuyhat, basename='ariza')
router.register(r'ariza-detail', HomiyDetailView, basename='ariza-detail')
router.register(r'talaba', TalabaQushishView, basename='talaba')
router.register(r'talaba-detail/<int:pk>', TalabaDetailView, basename='talaba-detail')

app_name = 'myapp'

urlpatterns = [

  
    path('', include(router.urls)),
    path('talabaid/<int:pk>/', TalabaDetailView.as_view(),name='talabaid')
   
 ]



 