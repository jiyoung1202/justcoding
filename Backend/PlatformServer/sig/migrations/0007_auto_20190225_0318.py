# Generated by Django 2.1.4 on 2019-02-25 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig', '0006_auto_20190225_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='band_cover_img_path',
            field=models.CharField(default='/media/static/t1.jpeg', max_length=200),
        ),
    ]
