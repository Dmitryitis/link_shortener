# Generated by Django 3.1.4 on 2020-12-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link_shortener', '0005_remove_link_short_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='short_link',
            field=models.CharField(default='', max_length=256, verbose_name='Короткая ссылка'),
            preserve_default=False,
        ),
    ]
