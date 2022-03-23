from django.db import models

class Endereco(models.Model):
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
    class Meta:
        abstract = True


class Contato(models.Model):
    email = models.CharField(
        max_length=50,
        blank=True,
    )
    telefone = models.CharField(max_length=12)

    class Meta:
        abstract = True


class PessoaFisica(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=40)
    cpf = models.IntegerField(unique=True)
    rg = models.IntegerField(
        unique=True,
        blank=True,
        null = True,
        )
    nascimento = models.DateField(
        'Data de Nascimento',
        blank = True,
        null = True,
    )
    naturalidade = models.CharField(
        max_length=30,
        blank = True,
    )

    class Meta:
        abstract = True