# Generated by Django 4.1.3 on 2022-12-12 18:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("talaba", "0006_alter_homiy_qushish_talabaga_homiy_tanla_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homiy_qushish_talabaga",
            name="homiy_tanla",
            field=models.CharField(
                choices=[("Tasdiqlandi", "Uzbek")], default="None", max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="talaba_qushish",
            name="sana",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 12, 18, 53, 49, 279147, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]