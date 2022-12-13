# Generated by Django 4.1.3 on 2022-12-12 19:08

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("talaba", "0008_alter_homiy_qushish_talabaga_homiy_tanla_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homiy_qushish_talabaga",
            name="homiy_tanla",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("Tasdiqlandi", "Uzbek"),
                    ("Tasdiqlandi", "nomalum"),
                    ("Tasdiqlandi", "nomalum ekan"),
                ],
                default="None",
                max_length=200,
            ),
        ),
        migrations.AlterField(
            model_name="talaba_qushish",
            name="sana",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 12, 19, 8, 39, 53032, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]