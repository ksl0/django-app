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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('lunch_points', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='foodie date')),
                ('participants', models.ForeignKey(to='connect.Friendship')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('signup_date', models.DateTimeField(blank=True, verbose_name='date signup')),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='friendship',
            name='from_friend',
            field=models.ForeignKey(related_name='friend_set', to='connect.PersonalProfile'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='to_friend',
            field=models.ForeignKey(related_name='to_friend_set', to='connect.PersonalProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('to_friend', 'from_friend')]),
        ),
    ]
