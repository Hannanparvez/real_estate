# Generated by Django 2.1.5 on 2019-02-08 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_comment_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Blog'),
        ),
    ]
