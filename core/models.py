from django.db import models

#Model Base que contem algums campos básicos para melhor organização do BD
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

#Model Pessoa utilizado para receber os dados de uma pessoa e cadastra-la no BD.
class Pessoa(Base):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length= 100)
    idade = models.IntegerField('Idade')
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=250, unique=True)
    apelido = models.CharField('Apelido', max_length=100, blank=True, null=True)
    observacao = models.CharField('Observação', max_length=300, blank=True, null=True)


