# Generated by Django 2.1.5 on 2019-02-08 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_reply_reply_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='reply_on',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog'),
            preserve_default=False,
        ),
    ]
