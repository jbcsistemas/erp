from django.urls import path
from .views import (
    FornecedorCreate,
    FornecedorList,
    FornecedorUpdate,
    FornecedorDelete,
    ProdutoCreate,
    ProdutoDelete,
    ProdutoList,
    ProdutoUpdate,
    )

app_name = 'produtos'
urlpatterns = [
    # Fornecedor
    path('fornecedores/novo/', FornecedorCreate.as_view(), name='novo-fornecedor'),
    path('fornecedores/', FornecedorList.as_view(), name='lista-fornecedor'),
    path('fornecedores/detalhes/<int:pk>/', FornecedorUpdate.as_view(), name='detalhes-fornecedor'),
    path('fornecedores/<int:pk>/delete/', FornecedorDelete.as_view(), name="delete-fornecedor"),
    # Produto
    path('', ProdutoList.as_view(), name='lista-produto'),
    path('novo/', ProdutoCreate.as_view(), name='novo-produto'),
    path('detalhes/<int:pk>/', ProdutoUpdate.as_view(), name='detalhes-produto'),
    path('<int:pk>/delete/', ProdutoDelete.as_view(), name='delete-produto'),
]