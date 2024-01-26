# Generated by Django 5.0.1 on 2024-01-24 04:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("etablissement", "0007_alter_etablissement_type_etablissement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="etablissement",
            name="type_etablissement",
            field=models.CharField(
                choices=[
                    ("college", "College"),
                    ("lycee", "Lycee"),
                    ("mixte", "Lycée Mixte"),
                    ("autre", "Autre"),
                ],
                default="autre",
                max_length=20,
                null=True,
            ),
        ),
    ]
