# Generated by Django 4.0.4 on 2022-07-19 15:16

from django.db import migrations, models
import med_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('med_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homiyqushish_talabaga',
            name='homiy',
            field=models.CharField(max_length=120, verbose_name=med_app.models.HomiyArizasi),
        ),
    ]