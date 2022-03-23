from django.db import models
from core.models import Contato, Endereco, PessoaFisica
from django.urls import reverse

class Setor(models.Model):
    nome = models.CharField(max_length=20)
    localizacao = models.CharField(max_length=20)


class Cargo(models.Model):
    nome = models.CharField(max_length=20)
    atribuicoes = models.CharField(max_length=40)
    setor = models.ForeignKey(
        'Setor',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )


class Cliente(Contato, Endereco, PessoaFisica):
    apelido = models.CharField(
        max_length=20,
        blank=True,
    )
    limite_credito = models.DecimalField(
        'Limite de Crédito',
        max_digits=8,
        decimal_places=2,
        default=0.00,
    )

    class Meta(Contato.Meta, Endereco.Meta, PessoaFisica.Meta):
        pass

    def get_absolute_url(self):
        return reverse('pessoas:detalhes-cliente',
            args=[self.pk]
        )


class Colaborador(Contato, Endereco, PessoaFisica):
    pis = models.IntegerField()
    numero_ctps = models.IntegerField('Número')
    serie_ctps = models.IntegerField('Série')
    admissao = models.DateField('Admissão')
    CBO = models.IntegerField()
    cargo = models.ForeignKey(
        'Cargo',
        on_delete=models.PROTECT,
    )
    cadastro = models.IntegerField()
    remuneracao = models.DecimalField(
        'Remuneração',
        max_digits=8,
        decimal_places=2,
    )

    class Meta(Contato.Meta, Endereco.Meta, PessoaFisica.Meta):
        pass
