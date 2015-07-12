# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lunch_points', models.IntegerField(blank=True, default=0)),
                ('from_friend', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='friend_set')),
                ('to_friend', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='to_friend_set')),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateTimeField(verbose_name='foodie date', auto_now=True)),
                ('participants', models.ForeignKey(to='connect.Friendship')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('signup_date', models.DateTimeField(blank=True, verbose_name='date signup')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('to_friend', 'from_friend')]),
        ),
    ]
