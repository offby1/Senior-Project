# Generated by Django 4.0.5 on 2022-08-31 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0011_alter_mapdatabase_m_address_alter_mapdatabase_m_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-m_added'], 'verbose_name': 'Video', 'verbose_name_plural': 'Videos'},
        ),
    ]
