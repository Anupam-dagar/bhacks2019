# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-09 06:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_question_bider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='bider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bider_for_a_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
