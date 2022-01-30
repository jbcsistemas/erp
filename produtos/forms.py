from django import forms
from produtos.models import Produto

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