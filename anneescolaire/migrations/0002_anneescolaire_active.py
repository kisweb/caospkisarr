# Generated by Django 5.0.1 on 2024-01-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anneescolaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anneescolaire',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
