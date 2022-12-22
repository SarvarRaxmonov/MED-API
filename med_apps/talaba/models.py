from django.db.models import (
    Model,
    CharField,
    DecimalField,
    DateTimeField,
    CASCADE,
    IntegerField,
)
from .managers import Talaba_All_managers, Homiy_add_to_talaba_managers
from django.db import models
from django.utils import timezone
from med_apps.homiy.models import HomiyArizasi
# Create your models here.

OTM_lar_ruyhati = [("OTM example", "OTM example")]


TALABALIK_turi = [
    ("Barchasi", "Barchasi"),
    ("Bakalavr", "Bakalavr"),
    ("Magistr", "Magistr"),
]


# Start of the talaba app modules


class Talaba_qushish(Model):
    Talaba_ismi = CharField(max_length=50, default="Nomalum", unique=True)
    telfon_raqam = DecimalField(max_digits=78, decimal_places=0, null=True)
    OTM = CharField(max_length=100, choices=OTM_lar_ruyhati, default="None")
    talabalik_turi = CharField(max_length=50, choices=TALABALIK_turi, default="None")
    Kontrakt_summa = DecimalField(max_digits=78, decimal_places=0, null=True)
    Ajratilgan_summa = DecimalField(max_digits=78, decimal_places=False, default=0)
    sana = DateTimeField(default=timezone.now)
    objects = Talaba_All_managers()

    # DIQQAT YANGI FIELD
    foizda = IntegerField(default=0)

    @property
    def talaba_kontrakti_tulanganlar(self):
        return self.Talaba_ismi.all()
    
    def save(self, *args, **kwargs):
        foizga_aylantirish = Talaba_qushish.objects.calculate_percentage(
            kontrakt=self.Kontrakt_summa, tushgan_summa=self.Ajratilgan_summa
        )
        self.foizda = foizga_aylantirish
        return super(Talaba_qushish, self).save(*args, **kwargs)

    def __str__(self):
        return self.Talaba_ismi
    
    class Meta:
        pass



class Homiy_qushish_talabaga(models.Model):
    homiy_tanla = models.ForeignKey(HomiyArizasi, on_delete=CASCADE, null=True)
    qancha_summa = models.DecimalField(max_digits=78, decimal_places=0, null=True)
    Talaba_Id = models.ForeignKey(
        Talaba_qushish, on_delete=CASCADE, null=True, related_name="talaba_homiysi"
    )
    objects = Homiy_add_to_talaba_managers()
    
    def __str__(self):
        return f"{self.homiy_tanla} {self.qancha_summa} UZS"
