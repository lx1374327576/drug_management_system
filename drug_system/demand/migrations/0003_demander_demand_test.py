# Generated by Django 2.2 on 2019-05-09 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0002_demander_demand'),
    ]

    operations = [
        migrations.AddField(
            model_name='demander_demand',
            name='test',
            field=models.IntegerField(default=0, verbose_name='test'),
        ),
    ]