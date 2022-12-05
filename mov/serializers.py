from attr import field, fields
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import HomiyArizasi, HomiyQushish_Talabaga , TalabaQushish

# Homiy ariza serializerlari ////////////////////////////

class HomiyArizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomiyArizasi
        fields = ['Shaxs_turi','Ismi','Telefon_raqami','Balans','tashkilot_nomi_yuridik_uchun']
        
        
class ArizaTopshirganlarSerializer(serializers.HyperlinkedModelSerializer):
    
        url = serializers.HyperlinkedIdentityField(view_name="myapp:ariza-detail")
 
        class Meta:
            model = HomiyArizasi
            fields = ['id','url','ariza_holati','Shaxs_turi','Ismi','Telefon_raqami','Balans','tashkilot_nomi_yuridik_uchun']
                                                            
class ArizaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomiyArizasi
        fields = '__all__'
 

# Talaba qushish serializerlari ////////////////////////////
         
class TalabaQushishSerializer(serializers.HyperlinkedModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(view_name="myapp:talaba-detail")
    
    class Meta:
        model = TalabaQushish
        fields = ['url','id','talaba_F_I_SH','telefon_raqami','OTM_ruyhati','Talabalik_turi','Kontrakt_summa','Ajratilgn_summa']
        
        
        
class TalabaDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TalabaQushish
        fields = '__all__'                 
        
        
class HomiyQushishTalabagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomiyQushish_Talabaga
        fields = ['homiy','beradigan_summa']    
        
        
           
        
class HyperSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="myapp:talabaid")
    
    class Meta:
        model = TalabaQushish
        fields = ['url','id','talaba_F_I_SH','telefon_raqami','OTM_ruyhati','Talabalik_turi','Kontrakt_summa','Ajratilgn_summa']
        
        depth = 1














        
        