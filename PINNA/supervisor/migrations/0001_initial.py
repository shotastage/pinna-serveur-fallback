# Generated by Django 2.0.2 on 2018-03-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_title', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
            ],
        ),
    ]