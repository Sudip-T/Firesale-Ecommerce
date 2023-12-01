# Generated by Django 4.2.7 on 2023-12-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(blank=True, max_length=200, null=True)),
                ("price", models.FloatField(max_length=50, null=True)),
                ("discounted_price", models.FloatField(blank=True, null=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("GA", "Gadgets"),
                            ("HA", "Home Appliances"),
                            ("MF", "Mens Fashions"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        choices=[
                            ("N", "new"),
                            ("BS", "best seller"),
                            ("SC", "stock clerance"),
                        ],
                        max_length=2,
                    ),
                ),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("description", models.TextField()),
            ],
        ),
    ]
