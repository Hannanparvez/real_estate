# Generated by Django 2.1.5 on 2019-02-06 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='is_team',
            field=models.BooleanField(default=False),
        ),
    ]