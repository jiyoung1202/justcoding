# Generated by Django 2.1.4 on 2019-02-23 15:04

from django.db import migrations, models
import file_manage.models


class Migration(migrations.Migration):

    dependencies = [
        ('file_manage', '0003_auto_20190223_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageinfo',
            name='photo_height',
        ),
        migrations.RemoveField(
            model_name='imageinfo',
            name='photo_width',
        ),
        migrations.AlterField(
            model_name='imageinfo',
            name='photo',
            field=models.ImageField(upload_to=file_manage.models.user_directory_path),
        ),
    ]
