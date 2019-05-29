# Generated by Django 2.2 on 2019-05-17 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0008_medicine_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='medicine_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='demand.Medicine_type'),
            preserve_default=False,
        ),
    ]