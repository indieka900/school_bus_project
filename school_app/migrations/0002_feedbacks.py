# Generated by Django 4.2.2 on 2023-06-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('joined', models.DateTimeField(auto_now_add=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]