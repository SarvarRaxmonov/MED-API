
from django.db import models

# Managerlar yozilishi mumkin bu yerga 

class HomiyArizlariNamelari(models.Manager):
    
    def get_queryset_of_ariza(self):
        
        return self.values('Ismi')
        
        
        