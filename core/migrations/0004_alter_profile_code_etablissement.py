# Generated by Django 5.0.1 on 2024-01-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_profile_code_etablissement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="code_etablissement",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
