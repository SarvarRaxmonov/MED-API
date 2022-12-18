from django.db import models
from med_apps.talaba.models import Talaba_qushish
# Managerlar yozilishi mumkin bu yerga 

class HomiyArizlariNamelari(models.Manager):
   
    def get_queryset_of_ariza(self):
        return super().get_queryset().filter(ariza_holati='Tasdiqlandi').values_list('Ismi',flat=True).order_by('-Balans')
        
    def update_ariza_balans(self,obj_name,summa):
        return super().get_queryset().filter(Ismi=obj_name).update(Balans=summa)   
    
    def balans_calculate(self,Ismi:str,summa:int):
        
        homiy_balans = super().get_queryset().get(Ismi=Ismi).values('Balans')
        if (homiy_balans - summa) != 0 :
             return summa
         return False
   
    def kontrakt_calculate(self,Id:int,summa:int):
          
        talaba_ajratilgan_summasi = Talaba_qushish.objects.get(id=Id).values('Ajratilgan_summa')
        talaba_kontrakt_summasi = Talaba_qushish.objects.get(id=Id).values('Kontrakt_summa')
        
        if (talaba_ajratilgan_summasi + summa) > talaba_kontrakt_summasi:
            return False
        else:
            return summa
        