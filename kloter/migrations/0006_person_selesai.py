# Generated by Django 2.2.6 on 2021-11-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kloter', '0005_person_telepon'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='selesai',
            field=models.BooleanField(default=False),
        ),
    ]
