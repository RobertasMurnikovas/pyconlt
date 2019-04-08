# Generated by Django 2.1.7 on 2019-04-04 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('committee_member', '0002_auto_20190318_1350'),
        ('proposals', '0002_new_fields_in_proposal_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Low'), (2, 'Above Low'), (3, 'Average'), (4, 'Above Average'), (5, 'High')], null=True, verbose_name='Rating')),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Done')], default=0, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('text', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='committee_member.CommitteeMember', verbose_name='Author')),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='proposals.Proposal', verbose_name='Proposal')),
            ],
        ),
    ]