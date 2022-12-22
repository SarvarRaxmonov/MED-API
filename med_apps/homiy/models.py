from django.db import models
from django.utils import timezone
from .managers import HomiyArizlariNamelari

# Create your models here.


Holat_buyicha = [
    ("Yangi", "Yangi"),
    ("Moderatsiyada", " Moderatsiyada"),
    ("Tasdiqlandi", "Tasdiqlandi"),
    ("Bekor qilingan", "Bekor qilingan"),
]


class HomiyArizasi(models.Model):
    Ismi = models.CharField(max_length=100, default="nomalum")
    Telefon_raqami = models.DecimalField(max_digits=78, decimal_places=0, null=True)
    Balans = models.DecimalField(max_digits=78, decimal_places=0, default="0")
    sana = models.DateTimeField(blank=True, null=True)

    # admin tomon tekshiradi
    Sarflangan_summa = models.DecimalField(max_digits=78, decimal_places=0, default="0")
    ariza_holati = models.CharField(
        max_length=30, choices=Holat_buyicha, default=Holat_buyicha[0][0]
    )
    objects = HomiyArizlariNamelari()

    # DIQQAT YANGI FIELDLAR MAN TOMONIDAN QUSHILGAN Automatic pul taqsimlovchi bu siz homiy ismi va
    # nechta talabaga pulni teng bulib bermoqchiligiyizni agar hohlasangiz 1 % dan 10 % (foizda olganda) gacha kontrakti
    # tulangan talabalarga va bundan yuqori foizlarda kontrakti tulangan talabalarga homiy mablag'ini teng taqsimlab beradi
    # agar ortib qolsa ortgan summa homiy balansiga qaytadi

    talaba_soni = models.IntegerField(default=0)
    kontrakt_tulangan_foizdan = models.FloatField(default=0)
    kontrakt_tulangan_foizgacha = models.FloatField(default=0)

    def __str__(self):
        return self.Ismi
