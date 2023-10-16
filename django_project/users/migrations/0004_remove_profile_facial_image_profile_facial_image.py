# Generated by Django 4.0.5 on 2022-07-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_facialimage_profile_facial_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Facial_Image',
        ),
        migrations.AddField(
            model_name='profile',
            name='facial_image',
            field=models.ImageField(default='defaultFace.jpg', upload_to='facial_images'),
        ),
    ]
