# Generated by Django 4.1.9 on 2024-01-16 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
