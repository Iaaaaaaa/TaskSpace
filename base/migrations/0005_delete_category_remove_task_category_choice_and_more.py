# Generated by Django 4.2.6 on 2023-11-26 06:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_task_category_task_category_choice'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='task',
            name='category_choice',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
