# Generated by Django 3.1.4 on 2020-12-11 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link_shortener', '0004_auto_20201212_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='short_link',
        ),
    ]
