# Generated by Django 4.1.3 on 2022-12-13 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("talaba", "0012_alter_talaba_qushish_sana"),
    ]

    operations = [
        migrations.AlterField(
            model_name="talaba_qushish",
            name="sana",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 13, 17, 58, 4, 541630, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
