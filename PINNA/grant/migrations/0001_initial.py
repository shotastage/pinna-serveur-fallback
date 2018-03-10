# Generated by Django 2.0.3 on 2018-03-10 17:57

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceCredential',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('credential', models.CharField(default='sX8Gf7oIPsXgsQ0EgHrhVjg4MAqY7-Bpr4Q0F7DCIlJMaFoz4yQmpHRFvejiZqIF35wnjOL0cbMjuIzHPc9M5w', max_length=255)),
                ('device_name', models.CharField(max_length=255)),
                ('useragent', models.CharField(max_length=255)),
                ('is_revoked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OneTapLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='QuGeOKYCOYkXkAwQYZHhH2AHk4jETuOU79rRzJeawYJKPIR496Nb_8pLs6c8kwmqC_yve34kPvBNl-7mEzA6BA', max_length=255)),
                ('is_tapped', models.BooleanField(default=False)),
                ('is_revoked', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PendingRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('verification_code', models.CharField(default='mgXq5NvNHKmemn-ymH-OgMbNfrxI0MutTGwvDPJzGFZLcGE7vl37SNqDuP7tdCmx8w3T-dbc3QMbygQadFwZPA', max_length=255)),
                ('is_revoked', models.BooleanField(default=False)),
            ],
        ),
    ]
