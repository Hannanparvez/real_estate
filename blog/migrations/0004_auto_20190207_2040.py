# Generated by Django 2.1.5 on 2019-02-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_blog_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_author',
            field=models.CharField(max_length=200),
        ),
    ]
