# Generated by Django 5.1.6 on 2025-02-07 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenditure',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='waste',
            name='user',
        ),
        migrations.DeleteModel(
            name='Energy',
        ),
        migrations.DeleteModel(
            name='Expenditure',
        ),
        migrations.DeleteModel(
            name='PersonalInfo',
        ),
        migrations.DeleteModel(
            name='Travel',
        ),
        migrations.DeleteModel(
            name='Waste',
        ),
    ]
