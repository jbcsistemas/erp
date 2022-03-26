from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from produtos.models import Fornecedor, Produto

from .forms import FornecedorForm, ProdutoForm

class ProdutoCreate(CreateView):
    template_name = 'produtos/produto_form.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('produtos:lista-produto')
    extra_context = {
        'previous_page': 'Produtos',
        'page_title': 'Novo Produto',
        'url_base': '/produtos',
    }


class ProdutoList(ListView):
    model = Produto
    paginate_by = 50
    extra_context = {
        'page_title': 'Produtos',
        'url_base': '/produtos',
    }


class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produtos/produto_update_form.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('produtos:lista-produto')


class ProdutoDelete(DeleteView):
    model = Produto
    success_url = '/produtos/'


class FornecedorCreate(CreateView):
    template_name = 'produtos/fornecedor_form.html'
    model = Fornecedor
    form_class = FornecedorForm
    success_url = reverse_lazy('produtos:lista-fornecedor')
    extra_context = {
        'previous_page': 'Fornecedores',
        'page_title': 'Novo Fornecedor',
        'url_base': '/produtos/fornecedores'
    }


class FornecedorList(ListView):
    model = Fornecedor
    paginate_by = 50
    extra_context = {
        'page_title': 'Fornecedores',
        'url_base': '/produtos/fornecedores'
    }


class FornecedorUpdate(UpdateView):
    model = Fornecedor
    template_name = 'produtos/fornecedor_update_form.html'
    form_class = FornecedorForm
    success_url = reverse_lazy('produtos:lista-fornecedor')


class FornecedorDelete(DeleteView):
    model = Fornecedor
    success_url = '/produtos/fornecedores/'