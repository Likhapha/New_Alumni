# Generated by Django 5.0.4 on 2024-06-13 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0015_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internshipapplication',
            name='university',
        ),
    ]
