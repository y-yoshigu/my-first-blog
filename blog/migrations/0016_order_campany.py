# Generated by Django 2.2.13 on 2020-11-09 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20201109_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='campany',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Campany'),
        ),
    ]