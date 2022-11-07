# Generated by Django 4.0.6 on 2022-10-30 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0004_rename_c_users_community_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('channel_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('channel_name', models.CharField(max_length=250)),
                ('admin', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='channeladmin', to=settings.AUTH_USER_MODEL)),
                ('community', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='channelcommunity', to='community.community')),
                ('users', models.ManyToManyField(related_name='channelusers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'channels',
            },
        ),
    ]