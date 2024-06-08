# Generated by Django 5.0.6 on 2024-06-08 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0003_economicsmcq_physicsmcq'),
    ]

    operations = [
        migrations.CreateModel(
            name='EconomicsAns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='', max_length=64)),
                ('ans', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicsAns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='', max_length=64)),
                ('ans', models.CharField(default='A', max_length=1)),
            ],
        ),
    ]
