# Generated by Django 4.1.3 on 2022-12-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HomiyArizasi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Ismi", models.CharField(default="nomalum", max_length=100)),
                (
                    "Telefon_raqami",
                    models.DecimalField(decimal_places=0, max_digits=78, null=True),
                ),
                (
                    "Balans",
                    models.DecimalField(decimal_places=0, default="0", max_digits=78),
                ),
                ("sana", models.DateTimeField(blank=True, null=True)),
                (
                    "Sarflangan_summa",
                    models.DecimalField(decimal_places=0, default="0", max_digits=78),
                ),
                (
                    "ariza_holati",
                    models.CharField(
                        choices=[
                            ("Yangi", "Yangi"),
                            ("Moderatsiyada", " Moderatsiyada"),
                            ("Tasdiqlandi", "Tasdiqlandi"),
                            ("Bekor qilingan", "Bekor qilingan"),
                        ],
                        default="Yangi",
                        max_length=30,
                    ),
                ),
                ("talaba_soni", models.IntegerField(default=0)),
                ("kontrakt_tulangan_foizdan", models.FloatField(default=0)),
                ("kontrakt_tulangan_foizgacha", models.FloatField(default=0)),
            ],
        ),
    ]
