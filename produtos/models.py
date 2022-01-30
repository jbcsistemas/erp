from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField(
        'Descrição',
        max_length=90,
    )


class Produto(models.Model):
    codigo_barras = models.CharField(
        'Código de barras',
        max_length=14,
        unique=True,
    )
    nome = models.CharField(
        max_length=40,
        db_index=True,
    )
    descricao = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )
    custo = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    preco = models.DecimalField(
        'Preço',
        max_digits=8,
        decimal_places=2,
    )
    slug = models.SlugField(
        max_length=200,
        db_index=True,
    )
    fabricante = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    categoria = models.ForeignKey(
        Categoria,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    disponivel = models.BooleanField(
        'Disponível',
        default=True,
    )

    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nome.upper()

