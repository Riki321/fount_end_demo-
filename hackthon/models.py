# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Organization(models.Model):
    org_id = models.CharField(primary_key=True, max_length=150)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150, blank=True, null=True)
    org_rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Organization'

        
class Participants(models.Model):
    part_id = models.CharField(primary_key=True, max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    mobile_no = models.CharField(max_length=150)
    address = models.CharField(max_length=150, blank=True, null=True)
    role = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150)
    disability = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Participants'
class Groups(models.Model):
    group = models.OneToOneField('Groups_datails', models.DO_NOTHING, primary_key=True)
    part = models.ForeignKey('Participants', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Groups'
        unique_together = (('group', 'part'),)


class Groups_datails(models.Model):
    group_id = models.CharField(primary_key=True, max_length=150)
    group_name = models.CharField(max_length=150)
    length = models.IntegerField()
    captian_first_name = models.CharField(max_length=150)
    captian_last_name = models.CharField(max_length=150)
    group_status = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Groups_datails'


class Hackthon(models.Model):
    hack_id = models.CharField(primary_key=True, max_length=150)
    org = models.ForeignKey('Organization', models.DO_NOTHING)
    hack_type = models.CharField(max_length=150)
    solo_or_team = models.CharField(max_length=150)
    rounds = models.IntegerField()
    how_long = models.CharField(max_length=150)
    hack_start_date = models.DateField()
    hack_end_date = models.DateField()
    venue = models.ForeignKey('Venue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Hackthon'


class Leaderbord(models.Model):
    lead_id = models.CharField(primary_key=True, max_length=150)
    rounds = models.ForeignKey('rounds_all_3_in_one', models.DO_NOTHING)
    round1_rank = models.IntegerField(blank=True, null=True)
    round2_rank = models.IntegerField(blank=True, null=True)
    round3_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Leaderbord'








class Prizes(models.Model):
    prize_id = models.CharField(primary_key=True, max_length=150)
    lead = models.ForeignKey(Leaderbord, models.DO_NOTHING)
    round1_prize = models.CharField(max_length=150, blank=True, null=True)
    round2_prize = models.CharField(max_length=150, blank=True, null=True)
    round3_prize = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Prizes'


class Problem(models.Model):
    prob_id = models.CharField(primary_key=True, max_length=150)
    prob_statement = models.CharField(max_length=150)
    coding_language = models.CharField(max_length=150, blank=True, null=True)
    difficulty_level = models.CharField(max_length=150)
    hack = models.ForeignKey(Hackthon, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Problem'


class Registration_2pkey(models.Model):
    hack = models.OneToOneField(Hackthon, models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey(Groups_datails, models.DO_NOTHING)
    reg_date = models.DateField()
    reg_time = models.TimeField()
    reg_end_date = models.DateField()
    reg_end_time = models.TimeField()
    group_limit = models.IntegerField()
    reg_status = models.CharField(max_length=150, blank=True, null=True)
    reg_limit = models.IntegerField(blank=True, null=True)
    request = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Registration_2pkey'
        unique_together = (('hack', 'group'),)


class rounds_all_3_in_one(models.Model):
    rounds_id = models.CharField(primary_key=True, max_length=150)
    hack = models.ForeignKey(Hackthon, models.DO_NOTHING)
    round1_type = models.CharField(max_length=150)
    round2_type = models.CharField(max_length=150)
    round3_type = models.CharField(max_length=150)
    group = models.ForeignKey(Groups_datails, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rounds_all_3_in_one'


class Sponsors(models.Model):
    spon_id = models.CharField(primary_key=True, max_length=150)
    name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'Sponsors'


class Sponsors_2pkey(models.Model):
    spon = models.OneToOneField(Sponsors, models.DO_NOTHING, primary_key=True)
    org = models.ForeignKey(Organization, models.DO_NOTHING)
    since = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sponsors_2pkey'
        unique_together = (('spon', 'org'),)


class Submission(models.Model):
    sub_id = models.CharField(primary_key=True, max_length=150)
    rounds = models.ForeignKey(rounds_all_3_in_one, models.DO_NOTHING)
    round1_sub_date = models.DateField()
    round1_status = models.CharField(max_length=150, blank=True, null=True)
    round2_sub_date = models.DateField()
    round2_status = models.CharField(max_length=150, blank=True, null=True)
    round3_sub_date = models.DateField()
    round3_status = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Submission'


class Venue(models.Model):
    venue_id = models.CharField(primary_key=True, max_length=150)
    venue_mode = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    arrive_date = models.DateField()
    arrive_time = models.TimeField()
    requirements = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Venue'


class Feedback(models.Model):
    org = models.OneToOneField(Organization, models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey(Groups_datails, models.DO_NOTHING)
    experience = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'
        unique_together = (('org', 'group'),)

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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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
    action_flag = models.SmallIntegerField()
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



