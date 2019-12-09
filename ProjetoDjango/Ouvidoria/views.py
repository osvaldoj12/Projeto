
from .forms import *
from django.shortcuts import render
from .models import Sugestoes, Denuncias, Reclamacoes, Elogios
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def Ouvidoria(request):
    return render(request,"templates/ExNav.html")

def sugestao(request):
    titulo = Sugestoes.object.order_by('codigo')
    context = {'titulo':titulo}
    return render(request,"templates/Sugestao/", context)

def denuncia(request):
    titulo = Denuncias.object.order_by('codigo')
    context = {'titulo':titulo}
    return render(request,"templates/Denuncia.html", context)

def reclamacoes(request):
    titulo = Reclamacoes.object.order_by('codigo')
    context = {'titulo':titulo}
    return render(request,"Ouvidoria/Reclamacoes.html", context)


def elogios(request):
    titulo = Elogios.object.order_by('codigo')
    context = {'titulo':titulo}
    return render(request,"templates/Elogios.html", context)

def Login(request):
    return render(request,"templates/registration/Login.html")

@login_required
def Cadastro(request):
    return render(request,"templates/registration/register.html")

@login_required
def RelatorioTotal(request):
    return render(request,"templates/RelatorioTotal.html")

@login_required
def RelatorioSugestao(request):
    return render(request,"templates/RelatorioSugestao.html")

@login_required
def RelatorioElogio(request):
    return render(request,"templates/RelatorioElogio.html")

@login_required
def RelatorioReclamacao(request):
    return render(request,"templates/RelatorioReclamacoes.html")

@login_required
def RelatorioDenuncias(request):
    return render(request,"templates/RelatorioDenuncia.html")

@login_required
def Home(request):
    return render(request,"templates/registration/telaLogin.html")

def get_name(request):
    if request.method == 'POST':
        form = SugestoesForm(request.POST)
        if form.is_valid():
            SugestoesForm = form.save(commit=False)
            SugestoesForm.save()
            return redirect('/')

    else:
        form = SugestoesForm()

    return render(request, 'Sugestao.html', {'form': form})

def get_name2(request):
    if request.method == 'POST':
        form = ReclamacoesForm(request.POST)
        if form.is_valid():
            ReclamacoesForm = form.save(commit=False)
            ReclamacoesForm.save()
            return redirect('/')

    else:
        form = ReclamacoesForm()

    return render(request, 'Reclamacoes.html', {'form': form})

def get_name3(request):
    if request.method == 'POST':
        form = ElogiosForm(request.POST)
        if form.is_valid():
            ElogiosForm = form.save(commit=False)
            ElogiosForm.save()
            return redirect('/')

    else:
        form = ElogiosForm()

    return render(request, 'Elogios.html', {'form': form})

def get_name4(request):
    if request.method == 'POST':
        form = DenunciasForm(request.POST)
        if form.is_valid():
            DenunciasForm = form.save(commit=False)
            DenunciasForm.save()
            return redirect('/')

    else:
        form = DenunciasForm()

    return render(request, 'Denuncia.html', {'form': form})
