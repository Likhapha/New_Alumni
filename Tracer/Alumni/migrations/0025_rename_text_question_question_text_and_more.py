# Generated by Django 5.0.4 on 2024-06-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0024_survey_target_audience_alter_question_question_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='is_required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='scale_range',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('radio', 'Radio'), ('checkbox', 'Checkbox'), ('dropdown', 'Dropdown'), ('rating', 'Rating'), ('date', 'Date')], max_length=10),
        ),
        migrations.AlterField(
            model_name='survey',
            name='target_audience',
            field=models.CharField(choices=[('alumni', 'Alumni'), ('students', 'Students')], max_length=100),
        ),
        migrations.AlterField(
            model_name='survey',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
