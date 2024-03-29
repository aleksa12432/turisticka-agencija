# Generated by Django 4.1.6 on 2023-02-10 17:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tripify", "0010_slike_smestaja"),
    ]

    operations = [
        migrations.CreateModel(
            name="Aranzman",
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
                ("naziv", models.CharField(max_length=256, unique=True)),
                ("opis", models.CharField(max_length=512)),
                (
                    "cena",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(3000),
                            django.core.validators.MinValueValidator(500),
                        ]
                    ),
                ),
                ("polazak", models.DateTimeField()),
                (
                    "duzina",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(14),
                            django.core.validators.MinValueValidator(7),
                        ]
                    ),
                ),
                (
                    "prevoz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tripify.tip_prevoza",
                    ),
                ),
                (
                    "smestaj",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tripify.tipovi_smestaja",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Termin",
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
                ("vreme_stizanja", models.DateTimeField()),
                (
                    "aranzman",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tripify.aranzman",
                    ),
                ),
                (
                    "smestaj",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tripify.smestaj",
                    ),
                ),
            ],
        ),
    ]
