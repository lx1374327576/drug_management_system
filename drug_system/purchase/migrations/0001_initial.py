# Generated by Django 2.2 on 2019-05-10 06:11

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
            name='Provider',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('due_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='due_time')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_time')),
                ('status', models.IntegerField(default=0, verbose_name='status')),
                ('check_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='check_time')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.Provider')),
            ],
        ),
    ]
