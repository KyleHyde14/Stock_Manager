from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('/')

    else:  
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('/')

    form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')