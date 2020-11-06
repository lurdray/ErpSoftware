# Generated by Django 3.1.2 on 2020-11-02 14:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20201031_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(default='none', max_length=150)),
                ('comment', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCommentConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.comment')),
                ('project', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='comments',
            field=models.ManyToManyField(through='project.ProjectCommentConnector', to='project.Comment'),
        ),
    ]