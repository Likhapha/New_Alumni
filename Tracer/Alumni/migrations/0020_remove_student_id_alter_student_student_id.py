# Generated by Django 5.0.4 on 2024-06-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0019_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, unique=True),
        ),
    ]
