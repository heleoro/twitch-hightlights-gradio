# Generated by Django 3.1.3 on 2021-03-09 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_link', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=200)),
                ('timestamp', models.CharField(max_length=200)),
                ('emotions', models.CharField(max_length=200)),
                ('coordinates', models.CharField(max_length=200)),
            ],
        ),
    ]