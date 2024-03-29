# Generated by Django 5.0.1 on 2024-01-28 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "etablissement",
            "0009_alter_etablissement_ief_alter_etablissement_save_by_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cotisation",
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
                ("montant", models.IntegerField(default=0, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name="etablissement",
            name="ief",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="iefs",
                to="etablissement.ief",
            ),
        ),
        migrations.AlterField(
            model_name="etablissement",
            name="save_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="etablissement",
            name="type_etablissement",
            field=models.CharField(
                choices=[
                    ("Collège", "Collège"),
                    ("Lycée", "Lycée"),
                    ("mixte", "Lycée Mixte"),
                    ("autre", "Autre"),
                ],
                default="autre",
                max_length=20,
                null=True,
            ),
        ),
    ]
