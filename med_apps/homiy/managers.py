from django.db import models

# Managerlar yozilishi mumkin bu yerga


class HomiyArizlariNamelari(models.Manager):
    def get_queryset_of_ariza(self):
        return (
            super()
            .get_queryset()
            .filter(ariza_holati="Tasdiqlandi")
            .values_list("Ismi", flat=True)
            .order_by("-Balans")
        )

    def update_ariza_balans(self, data: dict):
        ismi = data["Ismi"]
        summa = data["Balans"]
        sarflangan_summa = data["Sarflangan_summa"]

        return (
            super()
            .get_queryset()
            .filter(Ismi=ismi)
            .update(Balans=summa, Sarflangan_summa=sarflangan_summa)
        )

    def balans_calculate(self, Ismi: str, summa: int):

        homiy_balans = super().get_queryset().get(Ismi=Ismi)
        balans_minus = int(homiy_balans.Balans) - (summa)
        sarflangan_summa = int(homiy_balans.Sarflangan_summa) + (summa)
        if sarflangan_summa != 0:
            return dict(
                Ismi=Ismi, Balans=balans_minus, Sarflangan_summa=sarflangan_summa
            )

        return False
