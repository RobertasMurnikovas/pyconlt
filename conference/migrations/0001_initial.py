# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-30 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A name of the event e.g. PyConLT 2019', max_length=255)),
                ('url', models.CharField(help_text="The url path for the main page of the conference. e.g. '2018'", max_length=255)),
                ('date', models.DateField(blank=True, help_text='A date of the event or the date of the first day if the event spans more than one day.', null=True)),
                ('duration', models.IntegerField(blank=True, help_text='How many days the event spans', null=True)),
            ],
        ),
    ]
