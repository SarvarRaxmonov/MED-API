from django.db.models import (
    Model,
    CharField,
    DecimalField,
    DateTimeField,
    ForeignKey,
    CASCADE,
)
from med_apps.homiy.models import HomiyArizasi
from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone

# Create your models here.

OTM_lar_ruyhati = [("OTM example", "OTM example")]


TALABALIK_turi = [
    ("Barchasi", "Barchasi"),
    ("Bakalavr", "Bakalavr"),
    ("Magistr", "Magistr"),
]


# Mini managers for tlaaba module


class Talaba_All_managers(models.Manager):
    def kontrakt_calculate(self, Id: int, summa: int):

        talaba_malumotlari = super().get_queryset().get(id=Id)
        ajratilgan_summa = int(talaba_malumotlari.Ajratilgan_summa) + int(summa)
        if ajratilgan_summa > talaba_malumotlari.Kontrakt_summa:
            return False
        else:
            return dict(id=Id, Ajratilgan_summa=ajratilgan_summa)

    def update_talaba_balans(self, data: dict):
        id_talaba = data["id"]
        ajratilgan_pul_miqdori = data["Ajratilgan_summa"]
        return (
            super()
            .get_queryset()
            .filter(pk=id_talaba)
            .update(Ajratilgan_summa=ajratilgan_pul_miqdori)
        )


# Start of the talaba app modules


class Talaba_qushish(Model):
    Talaba_ismi = CharField(max_length=50, default="Nomalum", unique=True)
    telfon_raqam = DecimalField(max_digits=78, decimal_places=0, null=True)
    OTM = CharField(max_length=100, choices=OTM_lar_ruyhati, default="None")
    talabalik_turi = CharField(max_length=50, choices=TALABALIK_turi, default="None")
    Kontrakt_summa = DecimalField(max_digits=78, decimal_places=0, null=True)
    Ajratilgan_summa = DecimalField(max_digits=78, decimal_places=0, default=0)
    sana = DateTimeField(default=timezone.now())
    objects = Talaba_All_managers()

    @property
    def talaba_kontrakti_tulanganlar(self):
        return self.Talaba_ismi.all()

    def __str__(self):
        return self.Talaba_ismi

    class Meta:
        pass


class Homiy_qushish_talabaga(models.Model):
    homiy_tanla = models.CharField(max_length=200, default="None")
    qancha_summa = models.DecimalField(max_digits=78, decimal_places=0, null=True)
    Talaba_Id = models.ForeignKey(
        Talaba_qushish, on_delete=CASCADE, null=True, related_name="talaba_homiysi"
    )

    def __str__(self):
        return f"{self.homiy_tanla} {self.qancha_summa} UZS"
