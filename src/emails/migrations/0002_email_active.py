# Generated by Django 5.1.5 on 2025-01-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
