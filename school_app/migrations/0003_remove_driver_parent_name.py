# Generated by Django 4.2.2 on 2023-06-19 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0002_feedbacks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='parent_name',
        ),
    ]