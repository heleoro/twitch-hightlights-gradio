# Generated by Django 3.1.3 on 2021-03-09 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_stats'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stats',
            new_name='VideoStat',
        ),
    ]
