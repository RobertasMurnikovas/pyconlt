# Generated by Django 2.1.7 on 2019-04-16 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0005_auto_20190414_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='state',
            field=models.IntegerField(choices=[(0, 'Pending for approval'), (1, 'Approved'), (2, 'Rejected'), (3, 'Canceled')], default=0, help_text='Current state of proposal'),
        ),
    ]
