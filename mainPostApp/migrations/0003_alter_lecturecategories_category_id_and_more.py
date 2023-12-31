# Generated by Django 4.2.7 on 2023-11-14 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainPostApp', '0002_alter_totalcategories_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturecategories',
            name='category_id',
            field=models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='mainPostApp.totalcategories'),
        ),
        migrations.AlterField(
            model_name='totalcategories',
            name='top_category_code',
            field=models.ForeignKey(blank=True, max_length=20, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainPostApp.totalcategories'),
        ),
    ]
