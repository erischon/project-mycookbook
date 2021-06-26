from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from cookbook.models import Cookbook


class SignupPageView(generic.CreateView):
    """ Signup Page. """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
