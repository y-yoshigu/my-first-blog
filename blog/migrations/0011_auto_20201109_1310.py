# Generated by Django 2.2.13 on 2020-11-09 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201109_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='wishEnd_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='wishStart_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]