from django.db import migrations


def add_tipovi_prevoza(apps, schema_editor):
    Tip_prevoza = apps.get_model('tripify', 'Tip_prevoza')
    tipovi = [
        ("bus"),
        ("airplane"),
        ("ship"),
        ("train"),
        ("self transport")
    ]

    print("Popunjavam tipove prevoza...")

    Tip_prevoza.objects.bulk_create([Tip_prevoza(name=name) for name in tipovi])

class Migration(migrations.Migration):

    dependencies = [
        ("tripify", "0005_tipovi_smestaja_tipovi_sobe"),
    ]

    operations = [
        migrations.RunPython(add_tipovi_prevoza),
    ]
