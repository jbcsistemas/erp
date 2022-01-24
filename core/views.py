from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PainelView(LoginRequiredMixin, TemplateView):
    template_name = "core/painel.html"