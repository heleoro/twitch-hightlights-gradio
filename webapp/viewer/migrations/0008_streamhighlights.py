# Generated by Django 3.2 on 2021-04-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0007_stream_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamHighlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('stream_link', models.CharField(max_length=200)),
                ('highlights_urls', models.CharField(max_length=500)),
            ],
        ),
    ]