# Generated by Django 5.0.1 on 2024-03-04 22:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gestion", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facture",
            name="reference",
            field=models.CharField(default="zLXtotHI", max_length=120),
        ),
    ]