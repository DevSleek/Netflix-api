# Generated by Django 4.1.5 on 2023-02-23 03:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_alter_comment_send_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 8, 27, 43, 894886)),
        ),
    ]