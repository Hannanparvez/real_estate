# Generated by Django 2.1.5 on 2019-02-06 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_listing', '0004_testimonials'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='Testimonial',
        ),
    ]