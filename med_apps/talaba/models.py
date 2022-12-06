from django.db.models import Model, CharField, DecimalField, DateTimeField

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
      
      @property
      def talaba_kontrakti_tulanganlar(self):
          return self.Talaba_ismi.all()
      
          
                
          
      class Meta:
          pass                