# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reusable_blog', '0003_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
