from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from produtos.models import Produto

from .forms import ProdutoForm

class ProdutoCreate(CreateView):
    template_name = 'produtos/produto_form.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('core:painel')
