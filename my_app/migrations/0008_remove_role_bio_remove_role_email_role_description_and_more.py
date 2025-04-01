# Generated by Django 5.1.6 on 2025-04-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_rename_author_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='role',
            name='email',
        ),
        migrations.AddField(
            model_name='role',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='role',
            name='icon',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[('DUELIST', 'Duelist'), ('INITIATOR', 'Initiator'), ('CONTROLLER', 'Controller'), ('SENTINEL', 'Sentinel')], max_length=20, unique=True),
        ),
    ]
