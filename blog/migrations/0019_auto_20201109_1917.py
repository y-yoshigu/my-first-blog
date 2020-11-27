# Generated by Django 2.2.13 on 2020-11-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20201109_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='safeEnvironment_hazardous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safeEnvironment_heavy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safeWitness_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safeWitness_receipt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safeWitness_test',
            field=models.BooleanField(default=False),
        ),
    ]