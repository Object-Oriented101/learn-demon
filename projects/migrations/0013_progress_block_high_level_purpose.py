# Generated by Django 4.0.3 on 2022-04-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_rename_time_progress_block_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress_block',
            name='high_level_purpose',
            field=models.CharField(default='Testing manual added', max_length=1000),
            preserve_default=False,
        ),
    ]