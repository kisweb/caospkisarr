# Generated by Django 5.0.1 on 2024-03-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("etablissement", "0016_alter_etablissement_type_etablissement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tresorerie",
            name="mouvement",
            field=models.CharField(
                choices=[
                    ("Entree", "Entrée"),
                    ("Regularisation", "Régularisation"),
                    ("Attente", "Attente"),
                ],
                default="Entree",
                max_length=20,
                null=True,
            ),
        ),
    ]
