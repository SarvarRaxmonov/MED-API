# Generated by Django 4.1.3 on 2022-12-13 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("talaba", "0010_alter_homiy_qushish_talabaga_homiy_tanla_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="talaba_qushish",
            name="sana",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 13, 17, 34, 28, 912065, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
