# Generated by Django 5.0.1 on 2024-01-21 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anneescolaire", "0001_initial"),
        ("etablissement", "0002_alter_quote_save_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="annee_scolaire",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="anneescolaire.anneescolaire",
            ),
        ),
        migrations.AlterField(
            model_name="quote",
            name="etablissement",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="etablissement.etablissement",
            ),
        ),
    ]
