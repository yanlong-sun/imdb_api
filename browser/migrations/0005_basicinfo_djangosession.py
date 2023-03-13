# Generated by Django 4.1 on 2023-03-13 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0004_namebasics_titleakas_titlebasics_titleepisode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('tconst', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('titletype', models.TextField(blank=True, db_column='titleType', null=True)),
                ('primarytitle', models.TextField(blank=True, db_column='primaryTitle', null=True)),
                ('originaltitle', models.TextField(blank=True, db_column='originalTitle', null=True)),
                ('isadult', models.BooleanField(blank=True, db_column='isAdult', null=True)),
                ('startyear', models.DateField(blank=True, db_column='startYear', null=True)),
                ('endyear', models.DateField(blank=True, db_column='endYear', null=True)),
                ('runtimeminutes', models.TextField(blank=True, db_column='runtimeMinutes', null=True)),
                ('genres', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'basic_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
    ]
