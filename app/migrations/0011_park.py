# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-10-25 11:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_userinfo_areaname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('berthNumber', models.IntegerField(default=0)),
                ('inCount', models.IntegerField(default=0)),
                ('outCount', models.IntegerField(default=0)),
                ('cameraNumber', models.IntegerField(default=0)),
                ('isInSystem', models.BooleanField(default=False)),
                ('reason', models.CharField(max_length=200)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('passTime', models.DateTimeField(blank=True, null=True)),
                ('isPassed', models.BooleanField(default=False)),
                ('isLastest', models.BooleanField(default=False)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Area')),
                ('createUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createParkUser', to=settings.AUTH_USER_MODEL)),
                ('passUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='passParkUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '停车场',
                'verbose_name_plural': '停车场',
            },
        ),
    ]