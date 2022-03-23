from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, DeleteView

from pessoas.models import Cliente

from .forms import ClienteForm

class ClienteCreate(CreateView):
    template_name = 'pessoas/cliente_form.html'
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('pessoas:lista-cliente')


class ClienteList(ListView):
    model = Cliente
    paginate_by = 50


class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = 'pessoas/cliente_update_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('pessoas:lista-cliente')


class ClienteDelete(DeleteView):
    model = Cliente
    success_url = '/pessoas/clientes/'
