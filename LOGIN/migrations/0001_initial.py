# Generated by Django 3.2.21 on 2024-01-21 08:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8, 'password must  have 8 characters')])),
            ],
        ),
    ]
