# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-05 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0003_auto_20160405_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='image_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Image'),
        ),
    ]