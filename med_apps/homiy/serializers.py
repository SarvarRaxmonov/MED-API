from rest_framework import serializers
from .models import HomiyArizasi
from med_apps.talaba.models import Talaba_qushish
from django.utils import timezone
from rest_framework.serializers import ValidationError

# Homiy ariza serializerlari ////////////////////////////


class HomiyArizaSerializer(serializers.Serializer):

    Ismi = serializers.RegexField(regex=r"[a-zA-Z]$", allow_blank=False)
    Telefon_raqami = serializers.DecimalField(max_digits=78, decimal_places=0)
    Balans = serializers.DecimalField(max_digits=78, decimal_places=0)
    sana = serializers.HiddenField(default=timezone.now())

    class Meta:
        model = HomiyArizasi
        fields = ["Ism", "Telefon_raqam", "Balans", "sana", "url"]

    def create(self, validated_data):
        return HomiyArizasi.objects.create(**validated_data)

    def validate_Ismi(self, value):
        all_data = HomiyArizasi.objects.filter(Ismi=value)
        if all_data:
            raise serializers.ValidationError(
                "Uzur siz avval request yuborgansiz sizning survingiz kutish bulimida"
            )
        else:
            return value


class HomiyArizasiTahrirlash(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="myapp:ariza-detail", lookup_field="pk"
    )

    class Meta:
        model = HomiyArizasi
        fields = [
            "Ismi",
            "Balans",
            "sana",
            "Telefon_raqami",
            "Sarflangan_summa",
            "ariza_holati",
            "url",
        ]



class Homiy_pul_taqsimlash_Serialzier(serializers.ModelSerializer):
    Ismi = serializers.ChoiceField(
        choices=HomiyArizasi.objects.get_queryset_of_ariza()
    )
    talaba_soni = serializers.IntegerField()
    Balans = serializers.HiddenField(default=0)
    Sarflangan_summa = serializers.HiddenField(default=0)
    class Meta:
        model = HomiyArizasi
        fields = [
            'Ismi',
            'talaba_soni',
            'kontrakt_tulangan_foizdan',
            'kontrakt_tulangan_foizgacha',
            'Balans',
            'Sarflangan_summa'
        ]

    def validate_talaba_soni(self,value):
        jami_talabalar = Talaba_qushish.objects.get_all_talaba_count()
        if value > jami_talabalar:
            raise ValidationError(f"Bizda {value} ta talaba yuq siz noto'gri raqam kiritingiz") 
        return value
    
    def validate(self, attrs):
        foizdan = attrs['kontrakt_tulangan_foizdan']
        foizgacha = attrs['kontrakt_tulangan_foizgacha']
        shuncha_talaba_chiqadimi = Talaba_qushish.objects.auto_update_uchun_talabalar_soni_checking(attrs)
        if foizdan > 100 or foizgacha > 100:
            raise ValidationError("Iltimos foizni to'g'ri kiriting")
        elif shuncha_talaba_chiqadimi == False:
            raise ValidationError("Iltimos buncha kup talaba yuq bizda tulangan kontrakti")
        
        return attrs       
    
    def update(self, instance, validated_data):
        update_talaba = Talaba_qushish.objects.auto_update_talaba(data=validated_data)
        homiy_balans = HomiyArizasi.objects.auto_update_balans_calculate(Ismi=validated_data['Ismi'],qoldiq=update_talaba)
        if validated_data:
            validated_data['Sarflangan_summa'] = homiy_balans
            validated_data['Balans'] = update_talaba
        
        return super().update(instance, validated_data)
    
    