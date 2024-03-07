# Generated by Django 5.0.1 on 2024-03-04 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Commande",
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
                ("complete", models.BooleanField(blank=True, default=False, null=True)),
                ("transaction_id", models.CharField(max_length=200, null=True)),
                ("status", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "total_trans",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Personne",
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
                ("name", models.CharField(max_length=150)),
                ("phone", models.CharField(max_length=15, null=True)),
                (
                    "piece",
                    models.CharField(
                        choices=[("CNI", "Numéro CNI"), ("NINEA", "NINEA")],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "personne_type",
                    models.CharField(
                        choices=[
                            ("FOURNISSEUR", "Fournisseur"),
                            ("BENEFICIAIRE", "Bénéficiaire"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("numero", models.CharField(max_length=150, null=True)),
                ("address", models.CharField(blank=True, max_length=150, null=True)),
                ("service", models.CharField(blank=True, max_length=120, null=True)),
                ("locality", models.CharField(blank=True, max_length=70, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "personne",
                "verbose_name_plural": "personnes",
            },
        ),
        migrations.CreateModel(
            name="CommandeArticle",
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
                ("designation", models.CharField(max_length=200)),
                ("reference", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "quantite",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                ("prix", models.PositiveIntegerField(blank=True, default=0, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "commande",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="articles",
                        to="gestion.commande",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Facture",
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
                ("tva", models.PositiveIntegerField(default=10)),
                ("remise", models.PositiveIntegerField(default=0)),
                ("expedition", models.PositiveIntegerField(default=0)),
                ("paid", models.BooleanField(default=False)),
                (
                    "facture_type",
                    models.CharField(
                        choices=[
                            ("R", "RECU"),
                            ("P", "FACTURE PROFORMA"),
                            ("F", "FACTURE"),
                        ],
                        max_length=1,
                    ),
                ),
                ("reference", models.CharField(default="9gZnt1Hp", max_length=120)),
                ("comments", models.TextField(blank=True, max_length=1000, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "commande",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="commande",
                        to="gestion.commande",
                    ),
                ),
                (
                    "beneficiaire",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="factures",
                        to="gestion.personne",
                    ),
                ),
            ],
            options={
                "verbose_name": "Facture",
                "verbose_name_plural": "Factures",
            },
        ),
        migrations.AddField(
            model_name="commande",
            name="beneficiaire",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="gestion.personne",
            ),
        ),
    ]
