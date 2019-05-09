# Generated by Django 2.2 on 2019-05-09 11:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20190419_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_time')),
                ('status', models.IntegerField(default=0, verbose_name='status')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
