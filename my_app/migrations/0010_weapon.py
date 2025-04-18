# Generated by Django 5.1.6 on 2025-04-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_map_delete_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('fire_rate', models.CharField(max_length=100)),
                ('magazine_size', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.URLField()),
                ('alt_fire', models.CharField(max_length=200)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
