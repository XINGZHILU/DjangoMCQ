# Generated by Django 5.0.6 on 2024-06-08 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0011_delete_economicsstats_delete_physicsstats'),
    ]

    operations = [
        migrations.CreateModel(
            name='EconomicsStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='placeholder.png', max_length=64)),
                ('correct', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicsStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='placeholder.png', max_length=64)),
                ('correct', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
            ],
        ),
    ]
