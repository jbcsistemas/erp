from django.urls import path
from .views import ProdutoCreate

app_name = 'produtos'
urlpatterns = [
    path('cadastro/', ProdutoCreate.as_view(), name='cadastro-produto'),
]