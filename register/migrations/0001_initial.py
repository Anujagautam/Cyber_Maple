# Generated by Django 5.0.4 on 2024-04-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("full_name", models.CharField(max_length=30)),
                ("usern_name", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
                ("phone_no", models.IntegerField(max_length=15)),
                ("password", models.IntegerField(max_length=40)),
                ("con_password", models.IntegerField(max_length=40)),
            ],
        ),
    ]
