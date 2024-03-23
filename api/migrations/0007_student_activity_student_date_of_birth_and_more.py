# Generated by Django 5.0.2 on 2024-03-20 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_result_marks_result_subject_result_type_of_exam_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='activity',
            field=models.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='student',
            name='membership_in_organization',
            field=models.JSONField(default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='project',
            field=models.JSONField(default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('Chairman', 'Chairman'), ('Principal', 'Principal'), ('HOD', 'HOD'), ('Mentor', 'Mentor'), ('Student', 'Student')], max_length=20),
        ),
    ]