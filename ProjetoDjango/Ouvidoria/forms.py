from django import forms
from django.forms import ModelForm
from .models import *

class SugestoesForm(forms.ModelForm):

    class Meta:
        model = Sugestoes
        fields = ('titulo','comentarios')

class DenunciasForm(forms.ModelForm):
    
    class Meta:
        model = Denuncias
        fields = ('titulo','comentarios')

class ReclamacoesForm(forms.ModelForm):
    
    class Meta:
        model = Reclamacoes
        fields = ('titulo','comentarios')

class ElogiosForm(forms.ModelForm):
    
    class Meta:
        model = Elogios
        fields = ('titulo','comentarios')


