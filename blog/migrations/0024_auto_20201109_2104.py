# Generated by Django 2.2.13 on 2020-11-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20201109_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='safePretreatment_barricade',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safePretreatment_guard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safePretreatment_light',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safePretreatment_other',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='safePretreatment_rope',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safeProtecter_other',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
