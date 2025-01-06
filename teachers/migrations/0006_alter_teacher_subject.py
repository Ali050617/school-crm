# Generated by Django 5.1.4 on 2025-01-06 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_remove_subject_is_deleted'),
        ('teachers', '0005_remove_teacher_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='subjects.subject'),
        ),
    ]