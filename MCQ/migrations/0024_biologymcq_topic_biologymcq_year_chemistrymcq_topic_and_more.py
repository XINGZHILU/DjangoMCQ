# Generated by Django 5.0.6 on 2024-06-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0023_record_totalwrong'),
    ]

    operations = [
        migrations.AddField(
            model_name='biologymcq',
            name='topic',
            field=models.CharField(default='unclassified', max_length=64),
        ),
        migrations.AddField(
            model_name='biologymcq',
            name='year',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='chemistrymcq',
            name='topic',
            field=models.CharField(default='unclassified', max_length=64),
        ),
        migrations.AddField(
            model_name='chemistrymcq',
            name='year',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='economicsmcq',
            name='topic',
            field=models.CharField(default='unclassified', max_length=64),
        ),
        migrations.AddField(
            model_name='economicsmcq',
            name='year',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='physicsmcq',
            name='topic',
            field=models.CharField(default='unclassified', max_length=64),
        ),
        migrations.AddField(
            model_name='physicsmcq',
            name='year',
            field=models.IntegerField(default=0, max_length=4),
        ),
    ]