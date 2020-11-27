# Generated by Django 2.2.13 on 2020-11-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20201110_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='safePremeasure_gas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safePremeasure_removal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safePremeasure_switsh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='safePremeasure_valve',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='subjectDetail',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]