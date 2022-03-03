from django.urls import path
from .views import ProdutoCreate, ProdutoList, ProdutoUpdate

app_name = 'produtos'
urlpatterns = [
    path('', ProdutoList.as_view(), name='lista-produto'),
    path('cadastro/', ProdutoCreate.as_view(), name='cadastro-produto'),
    path('detalhes/<int:pk>/', ProdutoUpdate.as_view(), name='detalhes-produto')
]