from rest_framework import serializers
from .models import Talaba_qushish


class Talaba_Qushish_serializer(serializers.ModelSerializer):
    #   Talaba_ismi = serializers.CharField(max_length=50,default='Nomalum',unique=True)
    #   telfon_raqam = serializers.DecimalField(max_digits=78, decimal_places=0)
    #   OTM = serializers.CharField(max_length=100,choices=OTM_lar_ruyhati)
    #   talabalik_turi = serializers.CharField(max_length=50, choices=TALABALIK_turi)
    #   Kontrakt_summa = serializers.DecimalField(max_digits=78, decimal_places=0)     
      url = serializers.HyperlinkedIdentityField(view_name='myapp:talaba-detail',lookup_field='pk')     
      class Meta:
           model = Talaba_qushish
           fields = ['Talaba_ismi','telfon_raqam','OTM','talabalik_turi','Kontrakt_summa','url']
           
           
      def create(self, validated_data):
            return Talaba_qushish.objects.create(**validated_data)
      
    





  
  
