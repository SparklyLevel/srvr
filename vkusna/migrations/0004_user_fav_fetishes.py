# Generated by Django 5.1.2 on 2024-11-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkusna', '0003_ff_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fav_fetishes',
            field=models.ManyToManyField(related_name='users', to='vkusna.ff', verbose_name='ФавФетиши'),
        ),
    ]
