# Generated by Django 4.0.5 on 2022-08-28 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExamResults', '0007_rename_examresult_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='exam',
            new_name='m_exam',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='exam_Score',
            new_name='m_exam_Score',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='user',
            new_name='m_user',
        ),
    ]
