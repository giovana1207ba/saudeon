from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    telefone = forms.CharField(max_length=15, required=True)
    cpf = forms.CharField(max_length=11, required=True)
    numero_sus = forms.CharField(max_length=15, required=True)
    data_nascimento = forms.DateField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'telefone', 'cpf', 'numero_sus', 'data_nascimento', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True, label='Nome de Usuário')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Senha')


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['posto', 'medico', 'data', 'hora', 'observacao']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'observacao': forms.Textarea(attrs={'rows': 4}),
        }