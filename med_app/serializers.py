from rest_framework import serializers
from .models import HomiyArizasi

# Homiy ariza serializerlari ////////////////////////////

class HomiyArizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomiyArizasi
        fields = ['Shaxs_turi','Ismi','Telefon_raqami','Balans','tashkilot_nomi_yuridik_uchun']
        












        
        