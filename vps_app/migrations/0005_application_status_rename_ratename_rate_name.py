# Generated by Django 5.2 on 2025-04-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vps_app", "0004_remove_service_is_deleted_service_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Application_Status",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Статус заявки",
                "verbose_name_plural": "Статусы заявок",
            },
        ),
        migrations.RenameModel(
            old_name="RateName",
            new_name="Rate_Name",
        ),
    ]
