# Generated by Django 3.0.3 on 2020-04-13 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200413_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='hard',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.HardDisk'),
        ),
        migrations.AddField(
            model_name='computer',
            name='motherboard',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.MotherBoard'),
        ),
    ]