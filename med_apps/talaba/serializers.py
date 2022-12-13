from rest_framework import serializers
from .models import Talaba_qushish , Homiy_qushish_talabaga
from med_apps.homiy.models import HomiyArizasi

class Talaba_Qushish_serializer(serializers.ModelSerializer):
     
      url = serializers.HyperlinkedIdentityField(view_name='myapp:talaba-detail',lookup_field='pk')     
      class Meta:
           model = Talaba_qushish
           fields = ['Talaba_ismi','telfon_raqam','OTM','talabalik_turi','Kontrakt_summa','url']
     
     
      def create(self, validated_data):
          
          return Talaba_qushish.objects.create(**validated_data)
      
    
class Talabaga_homiy_qushish_serializer(serializers.ModelSerializer):
      homiy_tanla = serializers.ChoiceField(choices=HomiyArizasi.objects.get_queryset_of_ariza())
      qancha_summa = serializers.DecimalField(max_digits=78, decimal_places=0)
      Talaba_Ismi = serializers.CharField()

      class Meta:
           model = Homiy_qushish_talabaga
           fields = ['homiy_tanla','qancha_summa','Talaba_Ismi']



  
  
