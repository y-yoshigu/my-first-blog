# Generated by Django 2.2.13 on 2020-11-13 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20201113_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='acceptance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='clientApproval',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='comfirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='comfirmed_C',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='comfirmed_E',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='comfirmed_M',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='mescoReception',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safeApproval',
            field=models.BooleanField(default=False),
        ),
    ]