# Generated by Django 2.1.5 on 2019-02-08 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_on',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog'),
            preserve_default=False,
        ),
    ]
