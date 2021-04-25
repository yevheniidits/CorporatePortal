# Generated by Django 3.1.7 on 2021-04-14 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParagraphYoutubeVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255, null=True, verbose_name='ссылка на видео')),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='youtube_video', to='testing.paragraph', verbose_name='для параграфа')),
            ],
            options={
                'verbose_name': 'видео с Youtube',
            },
        ),
    ]