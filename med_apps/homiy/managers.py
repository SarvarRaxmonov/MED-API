
from django.db import models

# Managerlar yozilishi mumkin bu yerga 

class HomiyArizlariNamelari(models.Manager):
   
    def get_queryset_of_ariza(self):
        return super().get_queryset().filter(ariza_holati='Tasdiqlandi').values_list('Ismi',flat=True).order_by('-Balans')
        
    def update_ariza_balans(self,obj_name,summa):
        return super().get_queryset().filter(Ismi=obj_name).update(Balans=summa)   
        
        
        