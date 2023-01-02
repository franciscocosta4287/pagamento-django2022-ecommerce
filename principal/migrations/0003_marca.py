# Generated by Django 4.1.4 on 2022-12-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("principal", "0002_color_size"),
    ]

    operations = [
        migrations.CreateModel(
            name="Marca",
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
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="cat_imgs/")),
            ],
        ),
    ]