# Generated by Django 3.1.7 on 2021-05-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_confirmedmail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmedmail',
            name='mails_list',
            field=models.TextField(max_length=250),
        ),
    ]
