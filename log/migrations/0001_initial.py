# Generated by Django 4.2 on 2025-02-25 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="logdata_dong",
            fields=[
                ("seq", models.AutoField(primary_key=True, serialize=False)),
                ("time", models.CharField(max_length=255)),
                ("user_id", models.CharField(max_length=255)),
                ("servicemenu", models.CharField(max_length=255)),
                ("stars", models.CharField(max_length=255)),
                ("access_type", models.CharField(max_length=255)),
                ("reserve", models.CharField(max_length=255)),
            ],
        ),
    ]
