# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Aranzman(models.Model):
    naziv = models.CharField(max_length=32)
    napomena = models.TextField()

    class Meta:
        managed = False
        db_table = 'aranzman'


class AranzmanLokacija(models.Model):
    id_lokacije = models.ForeignKey('Lokacija', models.DO_NOTHING, db_column='id_lokacije')
    id_aranzmana = models.ForeignKey(Aranzman, models.DO_NOTHING, db_column='id_aranzmana')
    slika = models.TextField()

    class Meta:
        managed = False
        db_table = 'aranzman_lokacija'


class AranzmanPrevoz(models.Model):
    id_prevoza = models.ForeignKey('Prevoz', models.DO_NOTHING, db_column='id_prevoza')
    cena = models.DecimalField(max_digits=10, decimal_places=0)
    id_aranzmana = models.ForeignKey(Aranzman, models.DO_NOTHING, db_column='id_aranzmana')

    class Meta:
        managed = False
        db_table = 'aranzman_prevoz'


class AranzmanSlike(models.Model):
    id_lokacija = models.ForeignKey('Lokacija', models.DO_NOTHING, db_column='id_lokacija')
    id_aranzmana = models.ForeignKey(Aranzman, models.DO_NOTHING, db_column='id_aranzmana')

    class Meta:
        managed = False
        db_table = 'aranzman_slike'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Drzava(models.Model):
    naziv = models.CharField(max_length=60)
    oznaka = models.TextField()
    id_kontinenta = models.ForeignKey('Kontinent', models.DO_NOTHING, db_column='id_kontinenta')

    class Meta:
        managed = False
        db_table = 'drzava'


class KategorijaSmestaja(models.Model):
    tip_smestaja = models.TextField()

    class Meta:
        managed = False
        db_table = 'kategorija_smestaja'


class Kontinent(models.Model):
    naziv = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'kontinent'


class Korisnik(models.Model):
    id_role = models.ForeignKey('Role', models.DO_NOTHING, db_column='id_role')
    ime = models.TextField()
    prezime = models.TextField()

    class Meta:
        managed = False
        db_table = 'korisnik'


class Lokacija(models.Model):
    naziv = models.IntegerField()
    oznaka = models.IntegerField()
    id_drzave = models.ForeignKey(Drzava, models.DO_NOTHING, db_column='id_drzave')

    class Meta:
        managed = False
        db_table = 'lokacija'


class NacinPlacanja(models.Model):
    tip_placanja = models.TextField()

    class Meta:
        managed = False
        db_table = 'nacin_placanja'


class OpisSmestaja(models.Model):
    naziv_objekta = models.TextField()
    id_smestaja = models.ForeignKey('Smestaj', models.DO_NOTHING, db_column='id_smestaja')
    dodatak_u_sobi = models.IntegerField()
    id_aranzman = models.ForeignKey(Aranzman, models.DO_NOTHING, db_column='id_aranzman')
    id_kategorija_smestaja = models.ForeignKey(KategorijaSmestaja, models.DO_NOTHING, db_column='id_kategorija_smestaja')

    class Meta:
        managed = False
        db_table = 'opis_smestaja'


class Ponuda(models.Model):
    id_ponude = models.AutoField(primary_key=True)
    naziv = models.CharField(max_length=32)
    id_lokacije = models.ForeignKey(Lokacija, models.DO_NOTHING, db_column='id_lokacije')
    lokacija = models.TextField()
    opis_programa = models.TextField()
    slika = models.TextField()
    pocetak_putovanja = models.DateField()
    kraj_putovanja = models.DateField()
    cena = models.DecimalField(max_digits=10, decimal_places=0)
    id_prevoza = models.ForeignKey('Prevoz', models.DO_NOTHING, db_column='id_prevoza')
    id_aranzmana = models.ForeignKey(Aranzman, models.DO_NOTHING, db_column='id_aranzmana')

    class Meta:
        managed = False
        db_table = 'ponuda'


class Prevoz(models.Model):
    naziv = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'prevoz'


class ProgramPutovanja(models.Model):
    id_ponuda = models.ForeignKey(Ponuda, models.DO_NOTHING, db_column='id_ponuda')
    fakultativni_izleti = models.TextField()
    id_aranzmana = models.ForeignKey(Aranzman, models.DO_NOTHING, db_column='id_aranzmana')

    class Meta:
        managed = False
        db_table = 'program_putovanja'


class Putnik(models.Model):
    licna_karta = models.AutoField(primary_key=True)
    ime = models.TextField()
    prezime = models.TextField()
    kontakt_telefon = models.TextField()
    email = models.TextField()

    class Meta:
        managed = False
        db_table = 'putnik'


class Rezervacija(models.Model):
    br_rezervacije = models.AutoField(primary_key=True)
    id_nacin_placanja = models.ForeignKey(NacinPlacanja, models.DO_NOTHING, db_column='id_nacin_placanja')
    broj_osoba = models.IntegerField()
    komentar_napomena = models.TextField(db_column='komentar/napomena')  # Field renamed to remove unsuitable characters.
    status = models.IntegerField()
    licna_karta = models.ForeignKey(Putnik, models.DO_NOTHING, db_column='licna_karta')
    id_ponude = models.ForeignKey(Ponuda, models.DO_NOTHING, db_column='id_ponude')

    class Meta:
        managed = False
        db_table = 'rezervacija'


class Role(models.Model):
    naziv = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'role'


class SlikeSmestaja(models.Model):
    id_smestaja = models.ForeignKey('Smestaj', models.DO_NOTHING, db_column='id_smestaja')
    id_aranzman_lokacija = models.ForeignKey(AranzmanLokacija, models.DO_NOTHING, db_column='id_aranzman-lokacija')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'slike_smestaja'


class Smestaj(models.Model):
    naziv = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'smestaj'
