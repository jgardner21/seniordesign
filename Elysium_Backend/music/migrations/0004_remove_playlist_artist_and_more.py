# Generated by Django 5.0.1 on 2024-03-25 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_song_artist_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='artist_features',
        ),
    ]
