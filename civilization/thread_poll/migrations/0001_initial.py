# Generated by Django 2.1 on 2018-09-01 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('civforum', '0010_purpose_reverse'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='civforum.Thread')),
            ],
        ),
        migrations.CreateModel(
            name='ThreadPollACL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ThreadPollAT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ThreadPollChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_chosen', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ThreadPollOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thread_poll.ThreadPoll')),
            ],
        ),
        migrations.AddField(
            model_name='threadpollchoice',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thread_poll.ThreadPollOption'),
        ),
        migrations.AddField(
            model_name='threadpollchoice',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='threadpollacl',
            name='access_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thread_poll.ThreadPollAT'),
        ),
        migrations.AddField(
            model_name='threadpollacl',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thread_poll.ThreadPoll'),
        ),
        migrations.AddField(
            model_name='threadpollacl',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
