from django.db import models
from .managers import HomiyArizlariNamelari
# Create your models here.



Holat_buyicha = [
    ('Tasdiqlanmagan','Tasdiqlanmagan'),
    ('Tasdiqlandi','Tasdiqlandi')
]
 

OTM_lar_ruyhati = [
('OTM example','OTM example')

]

TALABALIK_turi = [
    ('Barchasi','Barchasi'),
    ('Bakalavr','Bakalavr'),
    ('Magistr','Magistr')
]
    

   
class HomiyArizasi(models.Model):
    Ismi = models.CharField(max_length=100,default='nomalum')
    Telefon_raqami = models.DecimalField(max_digits=78, decimal_places=0)
    Balans = models.DecimalField(max_digits=78, decimal_places=0, default='0')
    ariza_holati = models.CharField(max_length=30,choices=Holat_buyicha, default='Yangi')
    objects = HomiyArizlariNamelari()
      
    def __str__(self):
        return self.Ismi
    
    
    
