# Generated by Django 2.2.13 on 2020-11-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='subjectName',
        ),
        migrations.AddField(
            model_name='order',
            name='chargeName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='subProcess',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
