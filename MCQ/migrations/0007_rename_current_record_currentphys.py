# Generated by Django 5.0.6 on 2024-06-08 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0006_delete_economicsans_delete_physicsans_record_current'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='current',
            new_name='currentphys',
        ),
    ]
