# Generated by Django 4.0.5 on 2022-08-27 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_roommember_insession_alter_roommember_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roommember',
            old_name='name',
            new_name='m_name',
        ),
        migrations.RenameField(
            model_name='roommember',
            old_name='room_name',
            new_name='m_roomName',
        ),
        migrations.RenameField(
            model_name='roommember',
            old_name='uid',
            new_name='m_userID',
        ),
    ]
