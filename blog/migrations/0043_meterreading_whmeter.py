# Generated by Django 2.2.13 on 2021-01-13 07:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_auto_20201223_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whmeter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=30)),
                ('magnification', models.IntegerField(default=1)),
                ('unit', models.CharField(default='kWh', max_length=20)),
                ('maxvalue', models.IntegerField(default=0)),
                ('digits', models.IntegerField(default=4)),
                ('decimalPoint', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MeterReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integrated_Wh', models.FloatField(default=0)),
                ('readed_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reader', models.CharField(blank=True, max_length=20, null=True)),
                ('type', models.CharField(default=1, max_length=20)),
                ('count_year', models.IntegerField(default=2021)),
                ('count_month', models.IntegerField(default=1)),
                ('number', models.IntegerField(default=0)),
                ('Whmeter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Whmeter')),
            ],
        ),
    ]
