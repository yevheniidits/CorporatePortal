# Generated by Django 3.1.7 on 2021-03-22 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertestcase',
            name='date_expired',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 21, 39, 7, 165582), verbose_name='пройти до'),
        ),
    ]
