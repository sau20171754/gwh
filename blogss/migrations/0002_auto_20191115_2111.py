# Generated by Django 2.2.7 on 2019-11-15 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogss', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_time']},
        ),
    ]
