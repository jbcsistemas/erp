from django.urls import path
from pessoas.views import ClienteCreate, ClienteList, ClienteUpdate, ClienteDelete

app_name = 'pessoas'
urlpatterns = [
    path(
        'clientes/cadastro/',
        ClienteCreate.as_view(),
        name='cadastro-cliente',
    ),
    path(
        'clientes/',
        ClienteList.as_view(),
        name='lista-cliente',
    ),
    path(
        'clientes/detalhes/<int:pk>/',
        ClienteUpdate.as_view(),
        name='detalhes-cliente',
    ),
    path(
        'clientes/<int:pk>/delete/',
        ClienteDelete.as_view(),
        name='delete-fornecedor',
    ),
]