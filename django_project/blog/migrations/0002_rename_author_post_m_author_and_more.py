# Generated by Django 4.0.5 on 2022-08-28 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='m_author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='m_content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='m_date_posted',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='m_title',
        ),
    ]
