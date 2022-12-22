from django.db import models
import decimal
# Managerlar yozilishi mumkin bu yerga


class HomiyArizlariNamelari(models.Manager):
    def get_queryset_of_ariza(self):
        return (
            super()
            .get_queryset()
            .filter(ariza_holati="Tasdiqlandi",Balans__gte=1)
            .values_list("Ismi", flat=True)
            .order_by("-Balans")
        )

    def update_ariza_balans(self, data: dict):
        ismi = data["Ismi"]
        summa = data["Balans"]
        sarflangan_summa = data["Sarflangan_summa"]

        return (
            super()
            .get_queryset()
            .filter(ariza_holati="Tasdiqlandi",Ismi=ismi)
            .update(Balans=decimal.Decimal(summa), Sarflangan_summa=decimal.Decimal(sarflangan_summa))
        )

    def balans_calculate(self, Ismi: str, summa: int):

        homiy_balans = super().get_queryset().filter(ariza_holati="Tasdiqlandi").get(Ismi=Ismi)
        balans_minus = int(homiy_balans.Balans) - summa
        sarflangan_summa = int(homiy_balans.Sarflangan_summa) + int(summa)
        if str(balans_minus)[0] != '-':
            return dict(
                Ismi=Ismi, Balans=balans_minus, Sarflangan_summa=sarflangan_summa
            )
        return False
   
    def auto_update_balans_calculate(self,Ismi:str,qoldiq):
        homiy_balans = super().get_queryset().filter(ariza_holati="Tasdiqlandi").get(Ismi=Ismi)
        balans = ((int(homiy_balans.Balans) - int(qoldiq)) + int(homiy_balans.Sarflangan_summa))
        return balans
        
    
    def divide_homiy_balans_to_auto_update(self,Ismi,talaba_soni):
        homiy_balansi = super().get_queryset().filter(ariza_holati="Tasdiqlandi",Ismi=Ismi).values('Balans')
        har_bir_talabaga_teng_summa = homiy_balansi[0]['Balans'] / talaba_soni
        return har_bir_talabaga_teng_summa
        
        
        

    