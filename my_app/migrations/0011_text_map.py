# Generated by Django 5.1.6 on 2025-04-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_weapon'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='map',
            field=models.ManyToManyField(related_name='text', to='my_app.map'),
        ),
    ]
