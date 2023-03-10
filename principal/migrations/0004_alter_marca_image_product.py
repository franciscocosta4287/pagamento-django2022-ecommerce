# Generated by Django 4.1.4 on 2022-12-26 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("principal", "0003_marca"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marca",
            name="image",
            field=models.ImageField(upload_to="marca_imgs/"),
        ),
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
                ("title", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="product_imgs/")),
                ("slug", models.CharField(max_length=400)),
                ("datail", models.TextField()),
                ("specs", models.TextField()),
                ("price", models.PositiveIntegerField()),
                ("status", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="principal.category",
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="principal.color",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="principal.marca",
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="principal.size"
                    ),
                ),
            ],
        ),
    ]
