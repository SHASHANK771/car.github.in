# Generated by Django 3.1.5 on 2021-02-02 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='From1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25)),
                ('number', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=40)),
                ('carmodel', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='From2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25)),
                ('number', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=40)),
                ('address', models.CharField(blank=True, max_length=55)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('about', models.CharField(blank=True, max_length=25)),
                ('comment', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]