# Generated by Django 2.2.13 on 2020-12-22 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_auto_20201222_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='subProcess',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Subprocess'),
        ),
    ]