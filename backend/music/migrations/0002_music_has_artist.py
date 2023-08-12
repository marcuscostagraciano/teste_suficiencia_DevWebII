# Generated by Django 4.2.4 on 2023-08-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music_has_artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_artist', models.ManyToManyField(to='artist.artist')),
            ],
            options={
                'db_table': 'music_has_artist',
            },
        ),
    ]
