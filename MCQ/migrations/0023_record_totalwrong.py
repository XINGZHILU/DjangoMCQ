# Generated by Django 5.0.6 on 2024-06-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0022_rename_concord_record_official'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='totalwrong',
            field=models.IntegerField(default=0),
        ),
    ]
