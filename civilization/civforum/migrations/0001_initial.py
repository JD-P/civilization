# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 06:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ban_reason', models.TextField()),
                ('ban_date', models.DateTimeField()),
                ('ban_lifted', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BanType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2048)),
                ('creation_date', models.DateTimeField()),
                ('last_activity', models.DateTimeField()),
                ('locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PBMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50, null=True)),
                ('join_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2048)),
                ('creation_date', models.DateTimeField()),
                ('judge_date', models.DateTimeField(null=True)),
                ('probability', models.DecimalField(decimal_places=5, max_digits=6)),
                ('outcome', models.NullBooleanField(default=None)),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Board')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublicBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rigor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.DateTimeField()),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('posts', models.IntegerField()),
                ('creation_date', models.DateTimeField()),
                ('last_activity', models.DateTimeField()),
                ('locked', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Board')),
                ('rigor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Rigor')),
            ],
        ),
        migrations.CreateModel(
            name='TPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField()),
                ('body', models.CharField(max_length=57344)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Mood')),
            ],
        ),
        migrations.CreateModel(
            name='TPostAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=102400, upload_to='/attachments')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.TPost')),
            ],
        ),
        migrations.CreateModel(
            name='TPostPrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.TPost')),
                ('prediction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Prediction')),
            ],
        ),
        migrations.CreateModel(
            name='TPurpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Purpose')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Thread')),
            ],
        ),
        migrations.CreateModel(
            name='TRTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.RTag')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Thread')),
            ],
        ),
        migrations.AddField(
            model_name='tbody',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Thread'),
        ),
        migrations.AddField(
            model_name='rtag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Tag'),
        ),
        migrations.AddField(
            model_name='pbmembers',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.ProjectBoard'),
        ),
        migrations.AddField(
            model_name='pbmembers',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ban',
            name='ban_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.BanType'),
        ),
        migrations.AddField(
            model_name='ban',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
