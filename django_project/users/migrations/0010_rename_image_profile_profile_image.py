# Generated by Django 4.0.5 on 2022-08-30 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_m_facial_image_profile_facial_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='Profile_Image',
        ),
    ]
