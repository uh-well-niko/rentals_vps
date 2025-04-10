# Generated by Django 5.2 on 2025-04-10 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RateName",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.CharField(max_length=200)),
                ("mini_description", models.TextField()),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Rate",
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
                ("price", models.DecimalField(decimal_places=0, max_digits=10)),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rates",
                        to="vps_app.ratename",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rates",
                        to="vps_app.service",
                    ),
                ),
            ],
        ),
    ]
