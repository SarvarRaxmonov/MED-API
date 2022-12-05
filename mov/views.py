
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from yaml import serialize
from .serializers import HomiyArizaSerializer, ArizaTopshirganlarSerializer, HyperSerializer , TalabaQushishSerializer, HomiyQushishTalabagaSerializer
from .models import HomiyArizasi, TalabaQushish, HomiyQushish_Talabaga
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db.models import Sum
from mov import serializers
# Create your views here.



class UserViewSet(viewsets.ViewSet):
    serializer_class = HomiyArizaSerializer

    permission_classes = (permissions.AllowAny,)

    def list(self,request):
        
          queryset = HomiyArizasi.objects.first()
          serializer = HomiyArizaSerializer(queryset, many=False)
          
          return Response(serializer.data)
   
    def post(self, request):
        serializer = HomiyArizaSerializer(data=request.data)
        if serializer.is_valid():
          
            
            print('///////////////// ok ')
            
            
            serializer.save()
           
            return Response(serializer.data)
        return Response(serializer.errors, status = 'xatooo')
    
    def get_object(self, queryset=None, pk=None):
    
    
        return get_object_or_404(HomiyArizasi,id=pk)
        
class ArizaRuyhat(viewsets.ModelViewSet):
    
    serializer_class = ArizaTopshirganlarSerializer
    queryset = HomiyArizasi.objects.all()

class HomiyDetailView(viewsets.ModelViewSet):
     
     queryset = HomiyArizasi.objects.all()
     serializer_class = ArizaTopshirganlarSerializer

class TalabaQushishView(viewsets.ModelViewSet):
    
    serializer_class = TalabaQushishSerializer
    queryset = TalabaQushish.objects.all()
    

class DashboardView(viewsets.ReadOnlyModelViewSet):
    
    queryset = HomiyArizasi.objects.all()
    def list(self,request):
            
          queryset = HomiyArizasi.objects.aggregate(Sum('Balans'))
          queryset_two = TalabaQushish.objects.aggregate(Sum('Kontrakt_summa'))
          queryset_three = TalabaQushish.objects.aggregate(Sum('Ajratilgn_summa')) 
          return Response({'Homiylarning balans puli ':queryset,'Tulanmagan pular':queryset_two,'Tulangan pular':queryset_three})
         
    
################################## Talabag Homiy qushish joyi 


 


class TalabaDetailView(APIView):
     serializer_class = HomiyQushishTalabagaSerializer
     permission_classes = [AllowAny]
     
     def get_object(self,pk):
         try:
             return TalabaQushish.objects.get(id=pk)
         except TalabaQushish.DoesNotExist:
             raise Http404
     
     def get(self,request, pk, format=None):
         talaba = self.get_object(pk)
         serializer_context = {
             'request': request,
         }
         serializer = HyperSerializer(talaba,context={'request': request})
         return Response(serializer.data)
     
     def post(self, request, pk):
         
         
        serializer = HomiyQushishTalabagaSerializer(data=request.data,context={'request': request})
        
        if serializer.is_valid():
                   
                    homiy = HomiyArizasi.objects.filter(Ismi=serializer.validated_data['homiy'])
                    talaba = TalabaQushish.objects.filter(id=pk)
                    tulov = serializer.validated_data['beradigan_summa']
                    homiy_balans = homiy.values('Balans')[0]['Balans']
                
                    if homiy_balans - tulov >= 1:
            
                        if talaba.values('Kontrakt_summa')[0]['Kontrakt_summa'] >= talaba.values('Ajratilgn_summa')[0]['Ajratilgn_summa']+tulov:
                            homiy_pulidan = homiy_balans - tulov 
                            
                            talaba_balansiga = talaba.values('Ajratilgn_summa')[0]['Ajratilgn_summa'] + tulov
                            update_talaba = TalabaQushish.objects.get(id=pk)
                            update_homiy = HomiyArizasi.objects.get(Ismi=serializer.validated_data['homiy'])
                            
                            update_talaba.Ajratilgn_summa = talaba_balansiga
                            update_homiy.Balans = homiy_pulidan
                            update_talaba.save()
                            update_homiy.save()
                            
                            print('///////////////// ok ',pk,'............pkbu')

                            serializer.save()
                            
                            return Response(serializer.data)
                     
                        else:
                            return Response({'messages':'Kontrakt puli tulgan yoki kup pul qushyapsiz'})
                    else:
                         return Response({'messages':'PUL KAM BALNSDA'})
              
        return Response({'messages':'Tugri tuldiring'})
     
     @classmethod
     def get_extra_actions(cls):
          return []



class TalabaHomiyqushish(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = HyperSerializer
    queryset = TalabaQushish.objects.all()
         
        
    
   