from django import forms
from produtos.models import Fornecedor, Produto

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        exclude = ('slug',)
        widgets = {
            'cnpj': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingCNPJ',
                    'placeholder': 'CNPJ',
                }
            ),
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingNome',
                    'placeholder': 'Nome Empresarial',
                }
            ),
            'nome_fantasia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingFantasia',
                    'placeholder': 'Nome Fantasia',
                }
            ),
            'logradouro': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingLogradouro',
                    'placeholder': 'Logradouro',
                }
            ),
            'numero': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingNumero',
                    'placeholder': 'Número',
                }
            ),
            'complemento': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingComplemento',
                    'placeholder': 'Complemento',
                }
            ),
            'cep': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingCEP',
                    'placeholder': 'CEP',
                }
            ),
            'bairro': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'FloatingBairro',
                    'placeholder': 'Bairro',
                }
            ),
            'cidade': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'FloatingCidade',
                    'placeholder': 'Cidade',
                }
            ),
            'uf': forms.Select(
                attrs={
                    'class': 'form-select form-select-lg pb-3',
                    'aria-label': '.form-select-lg example',
                    'id': 'selectUF',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'FloatingEmail',
                    'placeholder': 'E-mail',
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'FloatingFone',
                    'placeholder': 'Telefone'
                }
            )
        }


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        exclude = ('slug',)
        widgets = {
            'codigo_barras': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingCodBarras',
                    'placeholder': 'Código de barras',
                }
            ),
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingNome',
                    'placeholder': 'Nome',
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingDesc',
                    'placeholder': 'Descrição',
                    'style': 'height: 100px;'
                }
            ),
            'custo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingCusto',
                    'min': '1',
                    'data-decimals': '0',
                    'placeholder': 'Custo R$'
                }
            ),
            'preco': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingPreco',
                    'min': '1',
                    'max': '1000000',
                    'placeholder': 'Preço R$',
                }
            ),
            'fabricante': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingFab',
                    'placeholder': 'Fabricante',
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingMarca',
                    'placeholder': 'Marca',
                }
            ),
            'categoria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingCate',
                    'placeholder': 'Categoria',
                }
            ),
            'disponivel': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'role': 'switch',
                    'id': 'flexSwitchCheckDisponivel',
                    'placeholder': 'Disponível',
                }
            ),
        }