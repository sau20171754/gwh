# Generated by Django 2.2.7 on 2019-11-17 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('read_stastic', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Read_Num',
            new_name='ReadNum',
        ),
    ]
