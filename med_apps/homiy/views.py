from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets            
from .serializers import HomiyArizaSerializer , HomiyArizasiTahrirlash, Homiy_pul_taqsimlash_Serialzier
from .models import HomiyArizasi
from rest_framework import permissions
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import filters   
from django_filters.rest_framework import DjangoFilterBackend 

# Create your views here.

class Homiy_malumotlari_access_Permissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['retrieve','put','update','delete']:
              return request.user.is_authenticated and request.user.is_staff        
        return True

class Homiy_arizasi(viewsets.ModelViewSet):
    permission_classes = [Homiy_malumotlari_access_Permissions]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]               
    search_fields = ['^ariza_holati']
    lookup_field = 'pk'
    
    def list(self,request):
          queryset = self.get_queryset()
          return Response({'MED':queryset})   
      
    def retrieve(self, request, pk=None):
        user = get_object_or_404(HomiyArizasi.objects.all(), pk=pk)
        serializer = HomiyArizasiTahrirlash(user,context={'request': request})
        return Response(serializer.data)
    
    def update(self, request, pk=None,*args, **kwargs):
        instance =  get_object_or_404(HomiyArizasi.objects.all(), pk=pk)
        serializer = HomiyArizasiTahrirlash(instance, data=request.data, context={'request': request} , partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data":serializer.data})    
    
    def post(self, request):
        serializer = HomiyArizaSerializer(data=request.data)
        if serializer.is_valid():    
            serializer.save()
            return Response({'Data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_200_OK)
    
    def get_serializer_class(self):
        if self.action == 'update':
            return HomiyArizasiTahrirlash
        else:
            return HomiyArizaSerializer
        
    def get_queryset(self):
      if self.action == 'list' or 'get':
          return []
      if self.action == 'put' or 'post':
          return HomiyArizasi.objects.all()  
    

class Homiy_all_data_for_filtering(viewsets.ModelViewSet):
    permission_classes = [Homiy_malumotlari_access_Permissions]
    serializer_class = HomiyArizasiTahrirlash
    queryset = HomiyArizasi.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]               
    search_fields = ['^Ismi']
    ordering_fields = ('sana',)


class Automatic_pul_taqsimlash_view(viewsets.ModelViewSet):
    permission_classes = [Homiy_malumotlari_access_Permissions]
    queryset = HomiyArizasi.objects.all()
    http_method_names = ['put','get']
    
    def get_queryset(self):
        if self.action in ['post','put']:
            return []
    def get_serializer_class(self):
        if self.action == 'update':
            return Homiy_pul_taqsimlash_Serialzier
        return Homiy_pul_taqsimlash_Serialzier   
    
    def put(self,request):   
        instance = HomiyArizasi.objects.filter(Ismi=request.data['Ismi'],ariza_holati='Tasdiqlandi').first()
        serializer = self.get_serializer(instance=instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)                  
    
        
       
        
        