# Generated by Django 5.0.1 on 2024-03-05 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("gestion", "0004_alter_facture_reference"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facture",
            name="reference",
            field=models.CharField(default="13AI9Qsg", max_length=120),
        ),
        migrations.CreateModel(
            name="Depense",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mouvement",
                    models.CharField(
                        choices=[
                            ("Sortie", "Sortie"),
                            ("Regularisation", "Régularisation"),
                            ("Attente", "Attente"),
                        ],
                        default="Sortie",
                        max_length=20,
                        null=True,
                    ),
                ),
                ("montant", models.PositiveIntegerField(default=0, null=True)),
                ("object_id", models.PositiveIntegerField(default=0, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["content_type", "object_id"],
                        name="gestion_dep_content_d00bbb_idx",
                    )
                ],
            },
        ),
    ]
