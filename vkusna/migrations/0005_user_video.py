# Generated by Django 5.1.2 on 2024-11-13 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkusna', '0004_user_fav_fetishes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='vkusna.video', verbose_name='Видосики'),
        ),
    ]
