# Generated by Django 3.2.13 on 2022-05-27 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpsblog', '0007_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=300, unique=True),
        ),
    ]
