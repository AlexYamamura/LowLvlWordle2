# Generated by Django 3.2.12 on 2022-02-13 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_alter_player_wordlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='wordlist',
            field=models.JSONField(null=True),
        ),
    ]
