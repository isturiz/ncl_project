from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

from .forms import CustomAuthenticationForm
 
def logout_view(request):
    logout(request)
    return redirect('../')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm
