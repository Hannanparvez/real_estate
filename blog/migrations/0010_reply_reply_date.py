# Generated by Django 2.1.5 on 2019-02-08 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190208_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='reply_date',
            field=models.DateField(default=datetime.date(2019, 2, 8)),
        ),
    ]