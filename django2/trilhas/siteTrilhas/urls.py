from django.urls import path
from siteTrilhas.views import *

# Create your views here.

urlpatterns = [
    path("", index, name="index"),
    path("variavel/", variavel, name="exibir_variavel"),
    path("cadastro/", variavel, name="cadastro_variavel"),
    path("itens/", imagem, name="cadastro_itens")
]