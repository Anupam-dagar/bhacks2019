# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-09 10:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0006_auto_20190309_0627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='bider',
        ),
        migrations.AddField(
            model_name='bider',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Question'),
        ),
        migrations.AddField(
            model_name='bider',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
