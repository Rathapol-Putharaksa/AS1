# Generated by Django 4.2.3 on 2023-07-07 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='TodoList',
        ),
    ]