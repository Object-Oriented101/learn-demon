# Generated by Django 4.0.3 on 2022-04-02 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_progress_block_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress_block',
            name='description',
            field=models.CharField(max_length=400),
        ),
    ]
