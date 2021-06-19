from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.translation import gettext as _


class CustomUserCreationForm(UserCreationForm):
    """ Custom User Form. """
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')
        labels = {
            'username': 'Prénom :',
            'email': 'Adresse mail :',
            'password1': 'Mot de passe :',
            'password2': 'Confirmez votre mot de passe :'
        }


class CustomUserChangeForm(UserChangeForm):
    """ Custom User Change Form. """
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
