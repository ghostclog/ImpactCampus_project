# Generated by Django 4.2.7 on 2023-11-09 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCommunityPost',
            fields=[
                ('post_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('post_contents', models.TextField()),
                ('reg_date', models.DateTimeField()),
                ('post_title', models.CharField(max_length=40)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.userdata')),
            ],
        ),
        migrations.CreateModel(
            name='RepostUserPost',
            fields=[
                ('report_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('report_contents', models.CharField(max_length=100)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userPostApp.usercommunitypost')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.userdata')),
            ],
        ),
    ]
