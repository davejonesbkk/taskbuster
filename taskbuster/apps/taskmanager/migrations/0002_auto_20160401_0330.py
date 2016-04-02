# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 01:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the project name', max_length=100, verbose_name='name')),
                ('color', models.CharField(default='#fff', help_text='Enter the hex color code, like #ccc or #cccccc', max_length=7, validators=[django.core.validators.RegexValidator('(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)')], verbose_name='color')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='taskmanager.Profile', verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'Projects',
                'ordering': ('user', 'name'),
                'verbose_name': 'Project',
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'name')]),
        ),
    ]
