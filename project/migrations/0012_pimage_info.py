# Generated by Django 3.1.2 on 2020-11-05 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20201104_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='pimage',
            name='info',
            field=models.TextField(default='none'),
        ),
    ]
