# Generated by Django 2.1.4 on 2019-02-24 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import file_manage.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '__first__'),
        ('file_manage', '0004_auto_20190223_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatImageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=file_manage.models.user_directory_path)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
