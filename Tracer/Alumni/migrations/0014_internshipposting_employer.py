# Generated by Django 5.0.4 on 2024-06-12 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0013_internshipapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipposting',
            name='employer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumni.employer'),
        ),
    ]
