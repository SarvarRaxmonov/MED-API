from django.db import models
from med_apps.homiy.models import HomiyArizasi
from django.core.exceptions import ObjectDoesNotExist


class Talaba_All_managers(models.Manager):
    def get_all_talaba_count(self):
        return super().get_queryset().count()

    def kontrakt_calculate(self, Id: int, summa: int):

        talaba_malumotlari = super().get_queryset().get(id=Id)
        ajratilgan_summa = int(talaba_malumotlari.Ajratilgan_summa) + int(summa)
        kontrakt_miqdori = talaba_malumotlari.Kontrakt_summa
        if ajratilgan_summa > talaba_malumotlari.Kontrakt_summa:
            return False
        else:
            return dict(
                id=Id,
                Ajratilgan_summa=ajratilgan_summa,
                Kontrakt_summa=kontrakt_miqdori,
            )

    def update_talaba_balans(self, data: dict):
        id_talaba = data["id"]
        Yangi_ajratilgan_pul_miqdori = data["Ajratilgan_summa"]
        foizga_aylantirish = self.calculate_percentage(
            kontrakt=data["Kontrakt_summa"], tushgan_summa=Yangi_ajratilgan_pul_miqdori
        )

        return (
            super()
            .get_queryset()
            .filter(pk=id_talaba)
            .update(
                Ajratilgan_summa=Yangi_ajratilgan_pul_miqdori, foizda=foizga_aylantirish
            )
        )

    def calculate_percentage(self, kontrakt, tushgan_summa):
        result = abs(tushgan_summa / kontrakt * 100)
        return result

    # YANGI MANAGERLAR AUTO TAQSIMLASH UCHUN

    def berilgan_foizga_tugri_kelgan_talabalar(self, data: dict):
        nechta_talaba = data["talaba_soni"]
        foizdan = data["kontrakt_tulangan_foizdan"]
        foizgacha = data["kontrakt_tulangan_foizgacha"]
        queryset = (
            super()
            .get_queryset()
            .filter(foizda__gte=foizdan, foizda__lte=foizgacha)
            .order_by("Ajratilgan_summa")[0:nechta_talaba]
        )

        return queryset

    def auto_update_uchun_talabalar_soni_checking(self, data: dict):
        queryset = self.berilgan_foizga_tugri_kelgan_talabalar(data=data)
        nechta_talaba = data["talaba_soni"]
        if queryset.count() != nechta_talaba:
            return False
        return True

    def auto_update_uchun_filterlangan_talabani_yangi_qiymatlari(
        self, data: dict, teng_summa: int
    ):
        qoldiq = 0
        kontrakt = data.Kontrakt_summa
        pr_Cal = self.calculate_percentage
        yangi_ajratilgan_summa = data.Ajratilgan_summa + teng_summa
        dicts = dict(
            Yangi_ajratilgan_summa=yangi_ajratilgan_summa,
            foizda=pr_Cal(kontrakt=kontrakt, tushgan_summa=yangi_ajratilgan_summa),
            qoldiq=qoldiq,
        )
        if yangi_ajratilgan_summa > kontrakt:
            ortgan_summa = yangi_ajratilgan_summa - kontrakt
            qoldiq = qoldiq + ortgan_summa
            teng_ajratilgan_summa = yangi_ajratilgan_summa - ortgan_summa
            dicts["Yangi_ajratilgan_summa"] = teng_ajratilgan_summa
            dicts["foizda"] = pr_Cal(
                kontrakt=kontrakt, tushgan_summa=teng_ajratilgan_summa
            )
            dicts["qoldiq"] = qoldiq

        return dicts

    def auto_update_talaba(self, data: dict):
        teng_summa = HomiyArizasi.objects.divide_homiy_balans_to_auto_update(
            Ismi=data["Ismi"], talaba_soni=data["talaba_soni"]
        )
        queryset = self.berilgan_foizga_tugri_kelgan_talabalar(data=data)
        qoldiq = 0
        for talaba in range(0, len(queryset)):
            data_talaba = self.auto_update_uchun_filterlangan_talabani_yangi_qiymatlari(
                data=queryset[talaba], teng_summa=teng_summa
            )
            if data_talaba["qoldiq"] > 0:
                qoldiq = qoldiq + data_talaba["qoldiq"]
            queryset[talaba].Ajratilgan_summa = data_talaba["Yangi_ajratilgan_summa"]
            queryset[talaba].foizda = data_talaba["foizda"]

        super().get_queryset().bulk_update(queryset, ["Ajratilgan_summa", "foizda"])

        return dict(ortib_qolgan_summa=qoldiq)


class Homiy_add_to_talaba_managers(models.Manager):
    def homiy_exists_or_not_i_database(self, data):
        Checking = True
        try:
            super().get_queryset().filter(
                homiy_tanla_id=data["homiy_tanla"], Talaba_Id_id=data["Talaba_Id"]
            ).exists()
        except ObjectDoesNotExist:
            Checking = False

        return Checking
