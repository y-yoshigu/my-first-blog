# Generated by Django 2.2.13 on 2020-12-22 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_apost_category_parentcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='subProcess',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Subprocess'),
        ),
    ]