# Generated by Django 2.2 on 2019-05-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0007_detail_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine_type',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
    ]