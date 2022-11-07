# Generated by Django 4.0.6 on 2022-11-03 13:26

import community.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0013_community_description_community_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='icon',
            field=models.ImageField(blank=True, upload_to=community.models.Community.nameFile),
        ),
        migrations.AlterField(
            model_name='community',
            name='poster',
            field=models.ImageField(blank=True, upload_to=community.models.Community.nameFile),
        ),
    ]