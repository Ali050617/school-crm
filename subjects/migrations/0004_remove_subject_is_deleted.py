# Generated by Django 5.1.4 on 2024-12-29 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_subject_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='is_deleted',
        ),
    ]