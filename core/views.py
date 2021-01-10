from django.views.generic import TemplateView,FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from core.forms import PessoaForm
from django.contrib import messages
from core.models import Pessoa
import requests


#Views utilizadas para formular cada página do site

#View que lista todas pessoas cadastradas no sistema
class ListagemView(TemplateView):
    #Utiliza o template listagem.html
    template_name = 'listagem.html'

    #Aqui é possível passar dados para o template, como por exemplo os dados de Pessoa que vem do BD
    def get_context_data(self, **kwargs):
        context = super(ListagemView, self).get_context_data(**kwargs)
        context['pessoa'] = Pessoa.objects.order_by('nome','sobrenome')
        return context

#View de Cadastro de Pessoas
class CadastroView(FormView):
    #Utiliza o form PessoaForm para cadastro, o template utilizado é o cadastro.html, e em casa de sucesso
    #do form, o site vai para a pagina listagem
    form_class = PessoaForm
    template_name = 'cadastro.html'
    success_url = reverse_lazy('listagem')

    #Método que toma uma ação caso o formulário seja válido, nesse caso ele salva o form no BD.
    def form_valid(self, form, *args, **kwargs):
        form.save()
        return super(CadastroView, self).form_valid(form, *args, **kwargs)

    #Caso o formulário seja inválido, ele dispara uma mensagem de erro.
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Não foi possível realizar o cadastro, tente novamente!')
        return super(CadastroView, self).form_invalid(form, *args, **kwargs)

    #Método que traz dados para o template
    def get_context_data(self, **kwargs):
        context = super(CadastroView, self).get_context_data(**kwargs)

        #Permite pegar os dados da API do site gerador-nomes
        request = requests.get('https://gerador-nomes.herokuapp.com/nome/aleatorio').text


        #Nessa parte é desenvolvido uma lógica para extração desses dados num tipo que seja possível utilizar nos templates
        #Essa lógica extrai todas as letras de request.text e transforma numa lista separando palavra por palavra
        a = request
        b = ''
        for y in a:
            for i in y:
                if i in "ÂÁÀÃÉÈÊÍÔÕÚQWERTYUIOPASDFGHJKLÇZXCVBNMâáàãéèêíôõúqwertyuiopasdfghjklçzxcvbnm":
                    b = b + i

        contador = 0
        c = ''
        for k in b:
            if contador == 0:
                c = c + k
                contador = contador + 1
            else:
                if k in 'ÂÁÀÃÉÈÊÍÔÕÚQWERTYUIOPASDFGHJKLÇZXCVBNM':
                    c = c + ' ' + k
                else:
                    c = c + k
        s = c.split()

        #Depois de aplicar toda a lógica, terá uma lista no qual é possível extrair o nome do primeiro index[0]
        #E o sobrenome dos index restante(Como a API gera um nome com dois sobrenomes, é possível pegar o sobrenome
        #usando o index [1] e [2]
        context['nome'] = s[0]
        context['sobrenome'] = s[1] + ' '+ s[2]
        return context

#View de atualização do Model Pessoa
class UpdatePessoaView(UpdateView):
    #Utiliza o model Pessoa, o template pessoa_upd.html e permite atualizar os campos descritos abaixo
    #Caso tenha sucesso em atualizar o form, o site vai para a página listagem
    model = Pessoa
    template_name = 'pessoa_upd.html'
    fields = ['nome', 'sobrenome', 'idade', 'data_nascimento','email','apelido','observacao']
    success_url = reverse_lazy('listagem')

    #Caso tenha problemas em atualizar o form, mostra uma mensagem de erro
    def form_invalid(self, form):
        messages.error(self.request, 'Não foi possível atualizar o cadastro, tente novamente!')
        return super(UpdatePessoaView, self).form_invalid(form)


#View para deletar uma pessoa do BD
class DeletePessoaView(DeleteView):
    #Utiliza o model pessoa, o template pessoa_del.html e caso tenha sucesso o site vai para a página listagem
    model = Pessoa
    template_name = 'pessoa_del.html'
    success_url = reverse_lazy('listagem')