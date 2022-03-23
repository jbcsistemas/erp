from django import forms
from pessoas.models import Cargo, Cliente, Colaborador, Setor

class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingNome',
                    'placeholder': 'Nome',
                }
            ),
            'localizacao': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingLocalizacao',
                    'placeholder': 'Localização',
                }
            ),
        }


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingNome',
                    'placeholder': 'Nome',
                }
            ),
            'atribuicoes': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingAtrib',
                    'placeholder': 'Atribuições',
                }
            ),
            'setor': forms.Select(
                attrs={
                    'class': 'form-select form-select-lg pb-3',
                    'aria-label': '.form-select-lg',
                    'id': 'selectSetor',
                }
            ),
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente 
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingNome',
                    'placeholder': 'Nome',
                }
            ),
            'sobrenome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingSobrenome',
                    'placeholder': 'Sobrenome',
                }
            ),
            'apelido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingApelido',
                    'placeholder': 'Apelido',
                }
            ),
            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingCPF',
                    'placeholder': 'CPF',
                }
            ),
            'rg': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingRG',
                    'placeholder': 'RG',
                }
            ),
            'nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingNasc',
                    'placeholder': 'dd/mm/aaaa',
                }
            ),
            'naturalidade': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingNatur',
                    'placeholder': 'Naturalidade',
                }
            ),
            'limite_credito': forms.NumberInput(
                attrs={
                    'id': 'InputLimiteCredito',
                    'placeholder': 'Limite de Crédito'
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
                    'id': 'floatingComp',
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
                    'id': 'floatingBairro',
                    'placeholder': 'Bairro',
                }
            ),
            'cidade': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingCidade',
                    'placeholder': 'Cidade',
                }
            ),
            'uf': forms.Select(
                attrs={
                    'class': 'form-select form-select-lg pb-3',
                    'aria-label': '.form-select-lg',
                    'id': 'selectUF',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingEmail',
                    'placeholder': 'E-mail',
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingFone',
                    'placeholder': 'Telefone/Celular'
                }
            )
        }
