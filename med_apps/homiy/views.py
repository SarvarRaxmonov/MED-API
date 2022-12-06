from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import HomiyArizaSerializer 
from .models import HomiyArizasi
from rest_framework import permissions
from rest_framework import status

# Create your views here.



class Homiy_arizasi(viewsets.ViewSet):
    serializer_class = HomiyArizaSerializer
    permission_classes = (permissions.AllowAny,)
    def list(self,request):
          queryset = HomiyArizasi.objects.first()
          serializer = HomiyArizaSerializer(queryset, many=False)
          return Response({"Misol ariza tuldirish uchun":serializer.data})

    def post(self, request):
        serializer = HomiyArizaSerializer(data=request.data)
        if serializer.is_valid():    
            serializer.save()
            return Response({'Data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_200_OK)
    
    def get_object(self, queryset=None, pk=None):
        return get_object_or_404(HomiyArizasi,id=pk)
        
    @classmethod
    def get_extra_actions(cls):
        return []
    
