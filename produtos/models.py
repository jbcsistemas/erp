from django.db import models
from django.urls import reverse

class Fornecedor(models.Model):
    UF_CHOICES = (
        ('ac', 'AC'),
        ('al', 'AL'),
        ('ap', 'AP'),
        ('am', 'AM'),
        ('ba', 'BA'),
        ('ce', 'CE'),
        ('df', 'DF'),
        ('es', 'ES'),
        ('go', 'GO'),
        ('ma', 'MA'),
        ('mg', 'MG'),
        ('ms', 'MS'),
        ('mt', 'MT'),
        ('pa', 'PA'),
        ('pb', 'PB'),
        ('pe', 'PE'),
        ('pi', 'PI'),
        ('pr', 'PR'),
        ('rj', 'RJ'),
        ('rn', 'RN'),
        ('rs', 'RS'),
        ('ro', 'RO'),
        ('rr', 'RR'),
        ('sc', 'SC'),
        ('se', 'SE'),
        ('sp', 'SP'),
        ('to', 'TO'),
    )
    cnpj = models.CharField(max_length=14)
    nome = models.CharField(
        'Nome Empresarial',
        max_length=50
        )
    nome_fantasia = models.CharField(
        'Nome Fantasia',
        max_length=50,
        blank=True
        )
    logradouro = models.CharField(
        max_length=30,
        blank=True,
        )
    numero = models.CharField(
        'Número',
        max_length=7,
        blank=True,
    )
    complemento = models.CharField(
        max_length=30,
        blank=True,
    )
    cep = models.CharField(
        max_length=9,
        blank=True,
    )
    bairro = models.CharField(
        'Bairro/Distrito',
        max_length=25,
        blank=True,
    )
    cidade = models.CharField(
        max_length=30,
        blank=True,
    )
    uf = models.CharField(
        max_length=2,
        choices=UF_CHOICES,
        blank=True,
    )
    email = models.CharField(
        max_length=50,
        blank=True,
    )
    telefone = models.CharField(
        max_length=12,
        blank=True,
    )
    slug = models.SlugField(max_length=250)

    def get_absolute_url(self):
        return reverse('produtos:detalhes-fornecedor',
           args=[self.pk]
        )



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

    def get_absolute_url(self):
        return reverse('produtos:detalhes-produto',
                       args=[self.pk]
        )

