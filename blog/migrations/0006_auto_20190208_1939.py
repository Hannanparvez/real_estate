# Generated by Django 2.1.5 on 2019-02-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190208_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_jist',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_title',
            field=models.CharField(max_length=200),
        ),
    ]
