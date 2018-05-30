# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20180513_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论列表', 'verbose_name_plural': '评论列表'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onefirst.Post', verbose_name='评论文章'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='评论信息'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='url',
            field=models.URLField(blank=True, verbose_name='URL'),
        ),
    ]