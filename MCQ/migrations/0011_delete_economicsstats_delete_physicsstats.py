# Generated by Django 5.0.6 on 2024-06-08 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MCQ', '0010_economicsstats_physicsstats'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EconomicsStats',
        ),
        migrations.DeleteModel(
            name='PhysicsStats',
        ),
    ]
