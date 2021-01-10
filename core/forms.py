from django import forms
from core.models import Pessoa

#Criação do formulário de cadastro, que se baseia no model Pessoa, e tem os seguintes fields(campos) abaixo
class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('nome', 'sobrenome', 'idade', 'data_nascimento', 'email', 'apelido', 'observacao')