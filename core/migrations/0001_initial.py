# Generated by Django 4.2.16 on 2024-09-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produto",
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
                (
                    "criado",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Criação"
                    ),
                ),
                (
                    "modificado",
                    models.DateField(auto_now=True, verbose_name="Data de Atualização"),
                ),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo?")),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "preco",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Preço"
                    ),
                ),
                ("estoque", models.IntegerField(verbose_name="Estoque")),
                (
                    "imagem",
                    models.ImageField(default="default.jpg", upload_to="products/"),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "slug",
                    models.SlugField(
                        blank=True, editable=False, max_length=100, verbose_name="Slug"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
