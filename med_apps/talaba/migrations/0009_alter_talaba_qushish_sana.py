# Generated by Django 4.1.3 on 2022-12-16 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("talaba", "0008_alter_talaba_qushish_sana"),
    ]

    operations = [
        migrations.AlterField(
            model_name="talaba_qushish",
            name="sana",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 16, 22, 35, 34, 488495, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
