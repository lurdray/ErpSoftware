# Generated by Django 3.1.2 on 2020-10-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20201030_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='material_issued',
            field=models.FileField(blank=True, upload_to='project/material_issues/'),
        ),
        migrations.AddField(
            model_name='project',
            name='material_requested',
            field=models.FileField(blank=True, upload_to='project/material_requested/'),
        ),
    ]
