# Generated by Django 4.2.7 on 2023-11-09 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('user_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('user_pass', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_tier', models.IntegerField()),
                ('is_manager', models.BooleanField(default=False)),
            ],
        ),
    ]
