from django.shortcuts import render

# Create your views here.

def index(request):
    lista = ['Raphael', 'Hadson', 'Rogerio', 'Eduardo', 'Kamylle']
    for i in lista:
        return render(request, i)  
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')