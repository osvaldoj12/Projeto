from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ouvidoria.urls')),
    path('', TemplateView.as_view(template_name='ExNav.html')),
    path('Sugestoes/', TemplateView.as_view(template_name='Sugestao.html')),
    path('Login/', TemplateView.as_view(template_name='Login.html')),
    path('Cadastros/', TemplateView.as_view(template_name='registration/Cadastro.html')),
    path('Denuncias/', TemplateView.as_view(template_name='Denuncia.html')),
    path('Reclamacoes/', TemplateView.as_view(template_name='Reclamacoes.html')),
    path('Elogios/', TemplateView.as_view(template_name='Elogios.html')),
    path('Relatorio de Elogios/', TemplateView.as_view(template_name='RelatorioElogio.html')),
    path('Relatorio de Reclamacoes/', TemplateView.as_view(template_name='RelatorioReclamacao.html')),
    path('Relatorio de Sugestoes/', TemplateView.as_view(template_name='RelatorioSugestao.html')),
    path('Relatorio de Denuncias/', TemplateView.as_view(template_name='RelatorioDenuncia.html')),
    path('Relatorio Total/', TemplateView.as_view(template_name='RelatorioTotal.html')),
    path('Home/', TemplateView.as_view(template_name='registration/telaLogin.html')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
