from rest_framework import serializers
from .models import HomiyArizasi
from django.utils import timezone

# Homiy ariza serializerlari ////////////////////////////

class HomiyArizaSerializer(serializers.Serializer):
    
      Ismi = serializers.RegexField(regex=r"[a-zA-Z]$",allow_blank=False)
      Telefon_raqami = serializers.DecimalField(max_digits=78, decimal_places=0)
      Balans = serializers.DecimalField(max_digits=78, decimal_places=0)      
      sana = serializers.HiddenField(default=timezone.now())
      class Meta:
            model = HomiyArizasi  
            fields=['Ism','Telefon_raqam','Balans']
        
      def create(self, validated_data):
            return HomiyArizasi.objects.create(**validated_data)
        
      def validate_Ismi(self,value):
            all_data = HomiyArizasi.objects.filter(Ismi=value)
            if all_data:
                  raise serializers.ValidationError("Uzur siz avval request yuborgansiz sizning survingiz kutish bulimida")  
            return value

       









        
        