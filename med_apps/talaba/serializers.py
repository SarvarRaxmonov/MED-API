from rest_framework import serializers
from .models import Talaba_qushish


class Talaba_Qushish_serializer(serializers.ModelSerializer):
    #   Talaba_ismi = serializers.CharField(max_length=50,default='Nomalum',unique=True)
    #   telfon_raqam = serializers.DecimalField(max_digits=78, decimal_places=0)
    #   OTM = serializers.CharField(max_length=100,choices=OTM_lar_ruyhati)
    #   talabalik_turi = serializers.CharField(max_length=50, choices=TALABALIK_turi)
    #   Kontrakt_summa = serializers.DecimalField(max_digits=78, decimal_places=0)          
      class Meta:
           model = Talaba_qushish
           fields = '__all__'
           
           
      def create(self, validated_data):
            return Talaba_qushish.objects.create(**validated_data)
      
    



