from django.contrib import admin
from Ouvidoria.models import Sugestoes, Elogios, Reclamacoes, Denuncias, Funcionario
# Register your models here.

admin.site.register(Sugestoes)
admin.site.register(Elogios)
admin.site.register(Reclamacoes)
admin.site.register(Denuncias)
admin.site.register(Funcionario)
