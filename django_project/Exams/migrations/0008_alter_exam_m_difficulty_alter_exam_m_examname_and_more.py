# Generated by Django 4.0.5 on 2022-08-31 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exams', '0007_rename_m_exam_name_exam_m_examname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='m_difficulty',
            field=models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Challenging', 'Challenging')], db_column='Difficulty', max_length=11),
        ),
        migrations.AlterField(
            model_name='exam',
            name='m_examName',
            field=models.CharField(db_column='Exam Name', max_length=120),
        ),
        migrations.AlterField(
            model_name='exam',
            name='m_material',
            field=models.CharField(db_column='Material', max_length=120),
        ),
        migrations.AlterField(
            model_name='exam',
            name='m_scoreRequiredToPass',
            field=models.IntegerField(db_column='Score Required To Pass', help_text='required score in %'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='m_timeLimit',
            field=models.IntegerField(db_column='Time Limit', help_text='duration of the exam in minutes'),
        ),
    ]
