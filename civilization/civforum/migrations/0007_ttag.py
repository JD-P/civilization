# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 07:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('civforum', '0006_tpost_thread'),
    ]

    operations = [
        migrations.CreateModel(
            name='TTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField()),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Tag')),
                ('tagger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Thread')),
            ],
        ),
    ]
