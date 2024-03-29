# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 08:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projectmanage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_md5', models.CharField(blank=True, default='', max_length=32)),
                ('type', models.CharField(choices=[('Video', (('feature', 'Feature'), ('trailer', 'Trailer'), ('preview', 'Preview'))), ('Audio', (('feataltaudio', 'Feature Alternate Audio'), ('featdesaudio', 'Feature Descriptive Audio'), ('trailaltaudio', 'Trailer Alternate Audio'), ('prevaltaudio', 'Preview Alternate Audio'))), ('Subtitle', (('featscc', 'Feature CC'), ('featitt', 'Feature ITT'), ('featsrt', 'Feature SRT'), ('trailscc', 'Trailer CC'), ('trailitt', 'Trailer ITT'), ('trailsrt', 'Trailer SRT'), ('prevscc', 'Preview CC'), ('previtt', 'Preview ITT'), ('prevsrt', 'Preview SRT'))), ('Poster Art', (('posteritunes', 'iTunes Poster Art'), ('postergoogle', 'Google Poster Art'), ('postersasktel', 'Sasktel Poster Art'), ('posternetflix', 'Netflix Poster Art'), ('posteramazon', 'Amazon Poster Art'), ('postermicro', 'Microsoft Poster Art')))], default='feature', max_length=25)),
                ('status', models.CharField(choices=[('Data Wrangling', (('datadownready', 'Ready for Download'), ('datadownloading', 'Downloading'), ('datadownloaded', 'Downloaded'), ('datacopyready', 'Ready for Copy'), ('datacopyinng', 'Copying'), ('datacopied', 'Copy Done'), ('dataupready', 'Ready for Upload'), ('datauploading', 'Uploading'), ('datauploaded', 'Uploaded'), ('dataupready', 'Ready for Upload'), ('datauploading', 'Uploading'), ('datauploaded', 'Uploaded'), ('dataarchready', 'Ready for Archival'), ('dataarchiving', 'Archiving'), ('dataarchived', 'Archived'))), ('inprod', 'In Production')], default='datadownready', max_length=25)),
                ('fichier', models.FileField(default='', upload_to='')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projectmanage.Project')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectmanage.Provider')),
            ],
        ),
    ]
