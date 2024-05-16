from django import forms
from django.forms import ModelForm
from .models import Pedidos, Usuarios, Itens

class PedidosForm(forms.ModelForm):
    class Meta:

        model = Pedidos
        fields = ["numero"]
        labels = {
            "numero": "numero1"
        }
        widgets = {
            'numero': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ex: 22",
                }
            ),
        }

class ItensForm(forms.ModelForm):
    class Meta:

        model = Itens
        fields = "__all__"
        labels = {
            "nome": "identificação",
            "preco": "valor",
            "path": "img",
        }
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ex: Arroz",
                }
            ),
            'preco': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ex: 9999.99",
                }
            ),
            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "foto",
                }
            ),
        }

class UsuariosForm(forms.ModelForm):
    class Meta:

        model = Usuarios
        fields = "__all__"
        labels = {
            'nome': "identificação",
            'email': "endereço",
        }
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ex: Raphel",
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ex: rapha@gmail.com",
                }
            )
        }