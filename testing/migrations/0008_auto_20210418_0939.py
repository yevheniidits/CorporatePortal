# Generated by Django 3.1.7 on 2021-04-18 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0007_auto_20210418_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraphyoutubevideo',
            name='source',
            field=models.CharField(max_length=255, null=True, verbose_name='ссылка на видео'),
        ),
    ]