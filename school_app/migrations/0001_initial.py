# Generated by Django 4.2.2 on 2023-06-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=60)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('joined', models.DateTimeField(auto_now_add=True, null=True)),
                ('parent_name', models.CharField(max_length=60)),
                ('phone_number', models.IntegerField()),
                ('bus_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('joined', models.DateTimeField(auto_now_add=True, null=True)),
                ('Class', models.IntegerField()),
                ('parent_name', models.CharField(max_length=60)),
                ('parent_email', models.EmailField(max_length=254)),
                ('bus_number', models.CharField(max_length=10)),
                ('password', models.CharField(default='', max_length=25)),
            ],
        ),
    ]
