# Generated by Django 4.1.6 on 2023-02-10 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tripify", "0011_aranzman_termin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aranzman",
            name="naziv",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]