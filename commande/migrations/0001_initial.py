# Generated by Django 5.0.1 on 2024-02-29 13:58

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Beneficiaire",
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
                ("numero", models.CharField(max_length=150, null=True)),
                ("address", models.CharField(blank=True, max_length=150, null=True)),
                ("service", models.CharField(blank=True, max_length=120, null=True)),
                ("locality", models.CharField(blank=True, max_length=70, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "beneficiaire",
                "verbose_name_plural": "beneficiaires",
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True, editable=False, populate_from="name"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "categorie",
                "verbose_name_plural": "categories",
            },
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
                ("facture_date_time", models.DateTimeField(auto_now_add=True)),
                ("total", models.PositiveIntegerField(default=0)),
                ("tva", models.PositiveIntegerField(default=10)),
                ("remise", models.PositiveIntegerField(default=0)),
                ("expedition", models.PositiveIntegerField(default=0)),
                ("last_updated_date", models.DateTimeField(blank=True, null=True)),
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
                ("reference", models.CharField(blank=True, max_length=120, null=True)),
                ("comments", models.TextField(blank=True, max_length=1000, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "beneficiaire",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="factures",
                        to="commande.beneficiaire",
                    ),
                ),
            ],
            options={
                "verbose_name": "Facture",
                "verbose_name_plural": "Factures",
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                ("name", models.CharField(max_length=200)),
                ("code", models.CharField(default="MvtrgJTH3K", max_length=32)),
                (
                    "order_type",
                    models.CharField(
                        choices=[
                            ("Produit", "Produit"),
                            ("Bien", "Bien"),
                            ("Service_Prestation", "Service et prestation"),
                            ("autre", "Autre"),
                        ],
                        default="autre",
                        max_length=20,
                        null=True,
                    ),
                ),
                ("valided_on", models.DateField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "facture",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="facture",
                        to="commande.facture",
                    ),
                ),
                (
                    "fournisseur",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="fournisseur",
                        to="commande.beneficiaire",
                    ),
                ),
            ],
            options={
                "verbose_name": "order",
                "verbose_name_plural": "orders",
            },
        ),
        migrations.CreateModel(
            name="Article",
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
                ("reference", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "unity",
                    models.CharField(
                        choices=[
                            ("1", "Unité"),
                            ("2", "Litre"),
                            ("3", "Kilogramme"),
                            ("4", "Carton"),
                            ("5", "Caisse"),
                            ("6", "En vrac"),
                        ],
                        default="1",
                        max_length=1,
                        null=True,
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=0)),
                ("unit_price", models.PositiveIntegerField(default=0)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("total", models.PositiveIntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="articles",
                        to="commande.category",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="articles",
                        to="commande.order",
                    ),
                ),
            ],
            options={
                "verbose_name": "article",
                "verbose_name_plural": "articles",
            },
        ),
    ]