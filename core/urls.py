from django.urls import path
from .views import ListagemView,CadastroView, UpdatePessoaView, DeletePessoaView

#Urls utilizadas na aplicação core
urlpatterns = [
    path('', CadastroView.as_view(), name='cadastro'),
    path('listagem', ListagemView.as_view(), name='listagem'),
    path('<int:pk>/update/', UpdatePessoaView.as_view(), name='upd_pessoa'),
    path('<int:pk>/delete/', DeletePessoaView.as_view(), name='del_pessoa'),
]