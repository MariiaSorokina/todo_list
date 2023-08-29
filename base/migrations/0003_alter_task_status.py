# Generated by Django 4.2.3 on 2023-08-26 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_task_options_remove_task_complete_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not started'), ('in_progress', 'In progress'), ('urgent', 'Urgent to complete'), ('completed', 'Completed')], default='not_started', max_length=20),
        ),
    ]
