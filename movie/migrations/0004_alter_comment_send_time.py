# Generated by Django 4.1.5 on 2023-02-22 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='send_time',
            field=models.DateField(default=datetime.datetime(2023, 2, 22, 15, 38, 0, 425247, tzinfo=datetime.timezone.utc)),
        ),
    ]
