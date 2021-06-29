from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, UsernameField
from django.utils.translation import gettext as _
from django import forms


class CustomUserCreationForm(UserCreationForm):
    """ Custom User Form. """
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')
        labels = {
            'username': 'Nom d\'utilisateur :',
            'email': 'Adresse email :',
            'password1': 'Mot de passe :',
            'password2': 'Confirmez votre mot de passe :'
        }


class CustomAuthenticationForm(AuthenticationForm):
    """ Custom Login Form. """
    username = UsernameField(
        label='Nom d\'utilisateur ',
        widget=forms.TextInput(attrs={'autofocus': True})
    )


class CustomUserChangeForm(UserChangeForm):
    """ Custom User Change Form. """
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
