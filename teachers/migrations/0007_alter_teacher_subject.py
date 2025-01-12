# Generated by Django 5.1.4 on 2025-01-06 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_remove_subject_is_deleted'),
        ('teachers', '0006_alter_teacher_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='subjects.subject'),
        ),
    ]
