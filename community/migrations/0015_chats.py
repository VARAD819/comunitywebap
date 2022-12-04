# Generated by Django 4.0.1 on 2022-12-03 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0014_alter_community_icon_alter_community_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('time', models.DateTimeField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channelchat', to='community.channels')),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useremail', to=settings.AUTH_USER_MODEL)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]