# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0002_auto_20161005_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'course_department_relationships',
            },
        ),
        migrations.CreateModel(
            name='CourseTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'course_teacher_relationships',
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='departments',
            field=models.ManyToManyField(through='mooc.CourseDepartment', to='mooc.Department'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(through='mooc.CourseTag', to='mooc.Tag'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(through='mooc.CourseTeacher', to='mooc.Teacher'),
        ),
        migrations.AddField(
            model_name='courseteacher',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooc.Course'),
        ),
        migrations.AddField(
            model_name='courseteacher',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooc.Teacher'),
        ),
        migrations.AddField(
            model_name='coursedepartment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooc.Course'),
        ),
        migrations.AddField(
            model_name='coursedepartment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mooc.Department'),
        ),
    ]