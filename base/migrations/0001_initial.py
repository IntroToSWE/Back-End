# Generated by Django 5.0.3 on 2024-04-09 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libraryPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('inside', models.BooleanField(default=True)),
                ('water', models.CharField(max_length=200)),
                ('sun', models.CharField(max_length=200)),
                ('fertilization', models.CharField(max_length=200)),
                ('soil', models.CharField(max_length=200)),
                ('pet', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=75)),
                ('last_name', models.CharField(blank=True, default='', max_length=75)),
                ('email', models.EmailField(blank=True, default='', max_length=150, unique=True)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='personalPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alive', models.BooleanField(default=False, null=True)),
                ('plantID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.libraryplant')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.users')),
            ],
        ),
    ]
