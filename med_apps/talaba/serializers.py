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
      Talaba_Id = serializers.HiddenField(default=0)

      class Meta:
           model = Homiy_qushish_talabaga
           fields = ['homiy_tanla','qancha_summa','Talaba_Id'] 
  
      def validate(self,data):
           qancha_summa = data['qancha_summa']
           talaba_idsi = data['Talaba_Id']
           homiy_balans = HomiyArizasi.objects.balans_calculate(Ismi=data['homiy_tanla'],summa=qancha_summa)
           talaba_balans = HomiyArizasi.objects.kontrakt_calculate(id=Talaba_idsi,summa=qancha_summa)
           if homiy_balans == False or talaba_balans == False:
               raise ValidationError("Summa juda ko'p")
           else:
                return data
      
      def create(self,validated_data):     
          if self.context.get("pk"):
               pk_of_talaba = Talaba_qushish.objects.get(id=self.context.get("pk"))
               validated_data['Talaba_Id'] = pk_of_talaba   
          return Homiy_qushish_talabaga.objects.create(**validated_data)

class Talaba_data_Read_Only_serializer(serializers.ModelSerializer):
      talaba_homiysi = serializers.StringRelatedField(many=True)     
      url = serializers.HyperlinkedIdentityField(view_name='myapp:talaba-detail',lookup_field='pk')     
      class Meta:
           model = Talaba_qushish
           fields = ['Talaba_ismi','telfon_raqam','OTM','talabalik_turi','Kontrakt_summa','url','talaba_homiysi']
          

      def get_fields(self, *args, **kwargs):
          fields = super().get_fields(*args, **kwargs)
          for field in fields:
                fields[field].read_only = True
          return fields
  
                                                                  