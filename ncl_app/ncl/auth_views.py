from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrecta.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


        
def logout_view(request):
    logout(request)
    return redirect('registration/home')
