# Generated by Django 2.2 on 2019-05-09 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0003_demander_demand_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demander_demand',
            name='test',
        ),
    ]
