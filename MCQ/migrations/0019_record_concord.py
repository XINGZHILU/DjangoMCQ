# Generated by Django 5.0.6 on 2024-06-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0018_record_biolsolved_record_biolwrong_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='concord',
            field=models.BooleanField(default=False),
        ),
    ]