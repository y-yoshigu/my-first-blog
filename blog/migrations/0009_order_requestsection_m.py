# Generated by Django 2.2.13 on 2020-11-09 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_order_subjectname'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='requestSection_M',
            field=models.BooleanField(default=False),
        ),
    ]
