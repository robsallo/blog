from django import forms
from django.contrib.auth import authenticate
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput
        (
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput
        (
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'email',
            'full_name',
            'ocupation',
            'genero',
            'date_birth',
        )
        widgets = {
            'email' : forms.EmailInput
            (
                attrs={
                    'placeholder' : 'Correo electrónico...',
                }
            ),
            'full_name' : forms.TextInput
            (
                attrs={
                    'placeholder' : 'Nombre completo...',
                }
            ),
            'ocupation' : forms.TextInput
            (
                attrs={
                    'placeholder' : 'Ocupación...',
                }
            ),
            'date_birth' : forms.DateInput
            (
                attrs={
                    'type' : 'date',
                }
            ),
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')
        return    

    def clean_full_name(self):
        full_name= self.cleaned_data['full_name']
        if not full_name.isalpha():
            self.add_error('full_name', 'Ingrese nombre válido')
        return full_name

class LoginForm(forms.Form):

    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput
        (
            attrs={
                'placeholder': 'Correo Electronico',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput
        (
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )