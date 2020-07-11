# Generated by Django 3.0.3 on 2020-04-13 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('manufacturer', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('model', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('type_of_product', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('socket', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('cpu', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('frequency', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('count_of_cores', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('ram', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('type_of_ram', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('gpu', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('color', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('os', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('power_supply', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('gabarites', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
