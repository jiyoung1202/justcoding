# Generated by Django 2.1.5 on 2019-02-11 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('nickname', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
            ],
        ),
    ]
