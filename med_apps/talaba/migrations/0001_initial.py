# Generated by Django 4.1.3 on 2022-12-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Talaba_qushish",
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
                ("Talaba_ismi", models.CharField(default="Nomalum", max_length=50)),
            ],
        ),
    ]