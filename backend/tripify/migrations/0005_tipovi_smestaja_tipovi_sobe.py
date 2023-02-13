from django.db import migrations

def add_tipovi_smestaja(apps, schema_editor):
    Tipovi_smestaja = apps.get_model('tripify', 'Tipovi_smestaja')
    tipovi = [
        ("hotel"),
        ("bungalow"),
    ]

    print("Popunjavam tipove smestaja...")

    Tipovi_smestaja.objects.bulk_create([Tipovi_smestaja(name=name) for name in tipovi])

def add_tip_sobe(apps, schema_editor):
    Tip_sobe = apps.get_model('tripify', 'Tip_sobe')
    tipovi = [
        ("1/1", 1),
        ("1/2", 2),
        ("1/3", 3),
        ("1/2+1", 3),
        ("1/3+1", 4),
        ("1/4", 4),
    ]

    print("Popunjavam tipove soba...")

    Tip_sobe.objects.bulk_create([Tip_sobe(name=name, broj_ljudi=broj_ljudi) for name, broj_ljudi in tipovi])

class Migration(migrations.Migration):

    dependencies = [
        ("tripify", "0004_tip_prevoza_tip_sobe_tipovi_smestaja"),
    ]

    operations = [
        migrations.RunPython(add_tipovi_smestaja),
        migrations.RunPython(add_tip_sobe),
    ]
