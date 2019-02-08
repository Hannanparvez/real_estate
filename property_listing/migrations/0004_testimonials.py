# Generated by Django 2.1.5 on 2019-02-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_listing', '0003_auto_20190206_0406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=200)),
                ('family_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('family_review', models.TextField()),
            ],
        ),
    ]