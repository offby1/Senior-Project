# Generated by Django 4.0.5 on 2022-08-28 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0005_alter_exam_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='difficulty',
            new_name='m_difficulty',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='exam_Name',
            new_name='m_exam_Name',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='material',
            new_name='m_material',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='question_Count',
            new_name='m_question_Count',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='score_Required_To_Pass',
            new_name='m_score_Required_To_Pass',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='time_Limit',
            new_name='m_time_Limit',
        ),
    ]
