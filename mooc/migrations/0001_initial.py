# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 04:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('chinese_name', models.CharField(max_length=255, unique=True)),
                ('grading', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('url', models.URLField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'MOOC'), (2, '\u804c\u4e1a\u8bfe\u7a0b')])),
                ('date_created', models.DateField()),
                ('date_status', models.DateField()),
                ('duration', models.PositiveSmallIntegerField()),
                ('followers_count', models.BigIntegerField()),
                ('introduction', models.TextField()),
                ('difficulty', models.SmallIntegerField(choices=[(0, '\u6682\u65e0'), (1, '\u7b80\u5355'), (2, '\u4e00\u822c'), (3, '\u56f0\u96be')])),
                ('first_lang', models.SmallIntegerField(choices=[(2, '\u4e2d\u6587'), (22, '\u4e4c\u514b\u5170\u8bed'), (9, '\u4fc4\u8bed'), (21, '\u514b\u7f57\u5730\u4e9a\u8bed'), (18, '\u5370\u5730\u8bed'), (12, '\u571f\u8033\u5176\u8bed'), (13, '\u5e0c\u4f2f\u6765\u8bed'), (6, '\u5fb7\u8bed'), (10, '\u610f\u5927\u5229\u8bed'), (7, '\u65e5\u8bed'), (4, '\u6cd5\u8bed'), (1, '\u82f1\u8bed'), (20, '\u8377\u5170\u8bed'), (11, '\u8461\u8404\u7259\u8bed'), (5, '\u897f\u73ed\u7259\u8bed'), (15, '\u963f\u62c9\u4f2f\u8bed'), (19, '\u97e9\u8bed'), (17, '\u9a6c\u6765\u8bed')])),
                ('second_lang', models.SmallIntegerField(choices=[(2, '\u4e2d\u6587'), (22, '\u4e4c\u514b\u5170\u8bed'), (9, '\u4fc4\u8bed'), (21, '\u514b\u7f57\u5730\u4e9a\u8bed'), (18, '\u5370\u5730\u8bed'), (12, '\u571f\u8033\u5176\u8bed'), (13, '\u5e0c\u4f2f\u6765\u8bed'), (6, '\u5fb7\u8bed'), (10, '\u610f\u5927\u5229\u8bed'), (7, '\u65e5\u8bed'), (4, '\u6cd5\u8bed'), (1, '\u82f1\u8bed'), (20, '\u8377\u5170\u8bed'), (11, '\u8461\u8404\u7259\u8bed'), (5, '\u897f\u73ed\u7259\u8bed'), (15, '\u963f\u62c9\u4f2f\u8bed'), (19, '\u97e9\u8bed'), (17, '\u9a6c\u6765\u8bed')])),
            ],
            options={
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='CourseTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooc.Course')),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=255, unique=True)),
                ('platform_site', models.URLField()),
                ('platform_wiki', models.TextField()),
            ],
            options={
                'db_table': 'platforms',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=255, unique=True)),
                ('country', models.CharField(max_length=3)),
                ('geo_lat', models.FloatField()),
                ('geo_lng', models.FloatField()),
            ],
            options={
                'db_table': 'schools',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
        migrations.AddField(
            model_name='coursetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooc.Tag'),
        ),
        migrations.AddField(
            model_name='course',
            name='departments',
            field=models.ManyToManyField(to='mooc.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooc.Platform'),
        ),
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooc.School'),
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(to='mooc.Tag'),
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(to='mooc.Teacher'),
        ),
    ]