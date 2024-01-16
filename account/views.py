from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect
from login_required import login_not_required
from .models import User


@login_not_required
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                auth_login(request, user)
                
                return redirect('/')

    return render(request, 'account/login.html')
@login_not_required
def logout_view(request):
    logout(request)
    return redirect('/login/')
    
@login_not_required
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            user = User.objects.create_user(name, email, password1)

            print('User created:', user)

            return redirect('/login/')
        else:
            print('Somethign went wrong')
    else:
        print('Just show the form!')

    return render(request, 'account/signup.html')

def profile(request, pk=None, **kwargs):
    return render(request, 'account/profile.html')