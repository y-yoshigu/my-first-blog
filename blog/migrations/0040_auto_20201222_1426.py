# Generated by Django 2.2.13 on 2020-12-22 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_auto_20201222_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='subProcess',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
