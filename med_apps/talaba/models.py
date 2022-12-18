from django.db.models import Model, CharField, DecimalField, DateTimeField, ForeignKey, CASCADE
from med_apps.homiy.models import HomiyArizasi
from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone
# Create your models here.

OTM_lar_ruyhati = [
('OTM example','OTM example')

]


TALABALIK_turi = [
    ('Barchasi','Barchasi'),
    ('Bakalavr','Bakalavr'),
    ('Magistr','Magistr')
]

class Talaba_qushish(Model):
      Talaba_ismi = CharField(max_length=50,default='Nomalum',unique=True)
      telfon_raqam = DecimalField(max_digits=78, decimal_places=0,null=True)
      OTM = CharField(max_length=100,choices=OTM_lar_ruyhati,default='None')
      talabalik_turi = CharField(max_length=50, choices=TALABALIK_turi,default='None')
      Kontrakt_summa = DecimalField(max_digits=78, decimal_places=0,null=True)          
      Ajratilgan_summa = DecimalField(max_digits=78, decimal_places=0,null=True)
      sana = DateTimeField(default=timezone.now()) 
     
      @property
      def talaba_kontrakti_tulanganlar(self):
          return self.Talaba_ismi.all()
      
      def __str__(self):
          return self.Talaba_ismi
          
      class Meta:
          pass                   

class Homiy_qushish_talabaga(models.Model):
      homiy_tanla = models.CharField(max_length=200,default='None')
      qancha_summa = models.DecimalField(max_digits=78, decimal_places=0,null=True)
      Talaba_Id = models.ForeignKey(Talaba_qushish,on_delete=CASCADE,null=True, related_name='talaba_homiysi')
     
      def __str__(self):
            return f"{self.homiy_tanla} {self.qancha_summa} UZS"
          
    
      
      
      