# Generated by Django 5.0.1 on 2024-03-01 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commande", "0005_alter_order_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facture",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="order",
                to="commande.order",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="code",
            field=models.CharField(default="pk0aQBvQwW", max_length=32),
        ),
    ]
