# Generated by Django 3.1.2 on 2020-10-31 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_project_supply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
