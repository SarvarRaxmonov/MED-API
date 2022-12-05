
from django.db import models
from .managers import HomiyArizlariNamelari
# Create your models here.

Shaxsning_turi = [
   ( 'Jismoniy shaxs','Jismoniy shaxs' ),
   ( 'Yuridik shaxs','Yuridik shaxs')
]
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
    

    

    

    


    

class LibUser(models.Model):
    name = models.CharField(max_length=100)
   
class HomiyArizasi(models.Model):
    Shaxs_turi = models.CharField(choices=Shaxsning_turi, max_length=20, default='None')
    Ismi = models.CharField(max_length=100,default='nomalum')
    Telefon_raqami = models.DecimalField(max_digits=78, decimal_places=0)

    Balans = models.DecimalField(max_digits=78, decimal_places=0, default='0')
    
   
    # Agar yurudik shaxs bulsa tashkilot nomini yozadi bulmasa default da no_company 
    tashkilot_nomi_yuridik_uchun = models.CharField(max_length=100,default='no_company')
    
    # Admin aniqlashtirishi uchun tasdiqlandi yoki bekor qilindi ariza 
    ariza_holati = models.CharField(max_length=30,choices=Holat_buyicha, default='Tasdiqlangani yuq')
    
    # Manageri manashu HomiyArizasini ismlarni qaytaradi
    objects = HomiyArizlariNamelari()
      
    def __str__(self):
        return self.Ismi
    
    
    
    
class TalabaQushish(models.Model): 
     
        talaba_F_I_SH = models.CharField(max_length=200, default='None')
        telefon_raqami = models.DecimalField(max_digits=78, decimal_places=0)
        OTM_ruyhati = models.CharField(choices=OTM_lar_ruyhati, default='Tanlanmadi', max_length=200)
        Talabalik_turi = models.CharField(choices=TALABALIK_turi, default='Tanlanmadi',max_length=200)
        Kontrakt_summa = models.DecimalField(max_digits=178, decimal_places=0)
        Ajratilgn_summa = models.DecimalField(max_digits=178, decimal_places=0, default='0')
        
        def __str__(self):
            return self.talaba_F_I_SH
        
        
class HomiyQushish_Talabaga(models.Model):
      
       homiy = models.ForeignKey(HomiyArizasi, on_delete=models.CASCADE)
       beradigan_summa = models.DecimalField(max_digits=178, decimal_places=0, default='0')
       
       
       
       