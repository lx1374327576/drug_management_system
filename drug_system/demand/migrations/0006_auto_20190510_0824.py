# Generated by Django 2.2 on 2019-05-10 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0005_auto_20190509_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='now_num',
            field=models.FloatField(default=0, verbose_name='now_num'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='total_num',
            field=models.FloatField(default=0, verbose_name='total_num'),
        ),
    ]
