# Generated by Django 5.0.4 on 2024-06-06 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0002_remove_jobposting_employer'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-01-01 00:00:00'),
            preserve_default=False,
        ),
    ]
