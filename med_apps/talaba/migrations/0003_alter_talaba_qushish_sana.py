# Generated by Django 4.1.3 on 2022-12-20 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("talaba", "0002_alter_talaba_qushish_sana"),
    ]

    operations = [
        migrations.AlterField(
            model_name="talaba_qushish",
            name="sana",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
