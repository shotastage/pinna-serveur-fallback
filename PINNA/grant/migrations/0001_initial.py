# Generated by Django 2.0.3 on 2018-03-12 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceCredential',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('credential', models.CharField(max_length=255)),
                ('device_name', models.CharField(max_length=255)),
                ('useragent', models.CharField(max_length=255)),
                ('is_revoked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GrantUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.UUIDField(default=uuid.uuid4)),
                ('account_secret', models.CharField(max_length=255)),
                ('account_type', models.CharField(choices=[('normal', 'Normal Type Account'), ('admin', 'Administrator'), ('guest', 'Guest Account'), ('super', 'Super User Account')], default='normal', max_length=10)),
                ('phone', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True)),
                ('birthday', models.DateField(blank=True)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('gender', models.IntegerField(choices=[(0, 'Not Defined'), (1, 'Male'), (2, 'Female'), (3, 'Other')], default=0)),
                ('profession', models.CharField(blank=True, max_length=255)),
                ('is_onetap_login_enabled', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OneTapLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('is_tapped', models.BooleanField(default=False)),
                ('is_revoked', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PendingResetAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.UUIDField(unique=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_revoked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SignupVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('verification_code', models.CharField(max_length=255)),
                ('is_revoked', models.BooleanField(default=False)),
            ],
        ),
    ]
