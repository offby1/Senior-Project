# Generated by Django 4.0.5 on 2022-06-30 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_is_facialimageset'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='facialImage',
            new_name='Facial_Image',
        ),
    ]
