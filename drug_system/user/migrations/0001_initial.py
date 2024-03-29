# Generated by Django 2.2 on 2019-04-19 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('user_name', models.CharField(max_length=20, unique=True, verbose_name='user_name')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_time')),
                ('is_admin', models.BinaryField(default=False, verbose_name='is_admin')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
                ('worker_type', models.IntegerField(default=0, verbose_name='worker_type')),
            ],
        ),
    ]
