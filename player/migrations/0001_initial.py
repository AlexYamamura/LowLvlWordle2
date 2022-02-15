# Generated by Django 3.2.12 on 2022-02-12 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess', models.CharField(max_length=5)),
                ('letterscorrect', models.CharField(max_length=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('win', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
