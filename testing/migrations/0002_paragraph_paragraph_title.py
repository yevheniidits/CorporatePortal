# Generated by Django 3.1.7 on 2021-05-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraph',
            name='paragraph_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='заголовок параграфа'),
        ),
    ]