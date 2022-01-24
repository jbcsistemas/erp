from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'caixa'
urlpatterns = [
    path('pdv/', TemplateView.as_view(template_name='caixa/pdv.html'),
         name='pdv'),
]