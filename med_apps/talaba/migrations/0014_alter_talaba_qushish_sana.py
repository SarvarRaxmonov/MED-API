# Generated by Django 4.1.3 on 2022-12-13 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("talaba", "0013_alter_talaba_qushish_sana"),
    ]

    operations = [
        migrations.AlterField(
            model_name="talaba_qushish",
            name="sana",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 13, 19, 28, 45, 48689, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
