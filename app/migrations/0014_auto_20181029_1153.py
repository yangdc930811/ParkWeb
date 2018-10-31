# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-29 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_park_islastest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='park',
            old_name='berthNumber',
            new_name='LEDNumber',
        ),
        migrations.RenameField(
            model_name='park',
            old_name='cameraNumber',
            new_name='computerNumber',
        ),
        migrations.RenameField(
            model_name='park',
            old_name='inCount',
            new_name='daozhaNumber',
        ),
        migrations.RenameField(
            model_name='park',
            old_name='outCount',
            new_name='fibre',
        ),
        migrations.RemoveField(
            model_name='park',
            name='area',
        ),
        migrations.RemoveField(
            model_name='park',
            name='isPassed',
        ),
        migrations.RemoveField(
            model_name='park',
            name='passTime',
        ),
        migrations.RemoveField(
            model_name='park',
            name='passUser',
        ),
        migrations.AddField(
            model_name='park',
            name='cameraBrand',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='park',
            name='company',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='park',
            name='daozhaBrand',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='park',
            name='explain',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='park',
            name='jiankongNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='park',
            name='jieshuncameraNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='park',
            name='ketuocameraNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='park',
            name='stationNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='park',
            name='wentongcameraNumber',
            field=models.IntegerField(default=0),
        ),
    ]