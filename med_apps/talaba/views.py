from rest_framework.response import Response
from rest_framework import views  
from .serializers import Talaba_Qushish_serializer
from rest_framework import status
from rest_framework.decorators import action
from .models import Talaba_qushish
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters      
from django_filters import rest_framework as filter_dj
from rest_framework.viewsets import ModelViewSet
# Create your views here.



class Talaba_qushish_view(ModelViewSet):
    serializer_class = Talaba_Qushish_serializer
    queryset = Talaba_qushish.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]               
    search_fields = ['^Talaba_ismi','talabalik_turi']
    ordering_fields = ('sana',)
 
    def get_queryset(self):
        if self.request.method == "POST":
            return []             
        return self.queryset
    
    @action(detail=False,methods=['post'])
    def add(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data_error)           
  
  