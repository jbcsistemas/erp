from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from produtos.models import Produto

from .forms import ProdutoForm

class ProdutoCreate(CreateView):
    template_name = 'produtos/produto_form.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('produtos:lista-produto')


class ProdutoList(ListView):
    model = Produto
    paginate_by = 50


class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produtos/produto_update_form.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('produtos:lista-produto')
