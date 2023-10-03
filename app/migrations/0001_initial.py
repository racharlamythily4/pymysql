# Generated by Django 4.2.3 on 2023-10-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Topic",
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
                ("topic_name", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
            ],
        ),
    ]
