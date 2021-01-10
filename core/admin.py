from django.contrib import admin

from .models import Pessoa

#Registro do model Pessoa na parte administrativa
@admin.register(Pessoa)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome','email','criados','modificado','ativo')
