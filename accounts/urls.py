from django.urls import path
from .views import SignupPageView, CustomLoginView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
