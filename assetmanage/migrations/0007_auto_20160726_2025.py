# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanage', '0006_auto_20160726_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='fichier',
        ),
        migrations.AddField(
            model_name='asset',
            name='file_name',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='asset',
            name='file_size',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='asset',
            name='file_location',
            field=models.FilePathField(default='', path='C:\\Users\\Simon\\Pictures\\poster_arts'),
        ),
    ]
