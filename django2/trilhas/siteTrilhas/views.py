from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def index(request):
    return render(request, 'site/index.html')

def variavel(request):
    form = UsuariosForm
    if request.method == "POST":
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
    
    x = Usuarios.objects.all()

    return render(request, "site/var.html", {'users':x, "form":form})

def imagem(request):
    form = ItensForm
    if request.method == "POST":
        form = ItensForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    x = Itens.objects.all()

    return render(request, "site/itens.html", {'users':x, "form":form})