# Generated by Django 2.1.5 on 2019-02-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig', '0002_auto_20190206_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandparticipate',
            name='is_band_leader',
            field=models.BooleanField(),
        ),
    ]
