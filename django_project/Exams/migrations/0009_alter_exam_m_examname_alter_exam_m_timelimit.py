# Generated by Django 4.0.5 on 2022-08-31 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0008_alter_exam_m_difficulty_alter_exam_m_examname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='m_examName',
            field=models.CharField(db_column='Exam_Name', max_length=120),
        ),
        migrations.AlterField(
            model_name='exam',
            name='m_timeLimit',
            field=models.IntegerField(db_column='Time_Limit', help_text='duration of the exam in minutes'),
        ),
    ]
