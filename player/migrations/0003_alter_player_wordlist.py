# Generated by Django 3.2.12 on 2022-02-12 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20220212_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='wordlist',
            field=models.TextField(blank=True),
        ),
    ]
