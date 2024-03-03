from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect
from login_required import login_not_required
from .forms import FilterUserForm
from .filters import UserFilterSet
from .models import User


@login_not_required
def login(request):
    filterset = UserFilterSet(request.GET, queryset=User.objects.all()) 
    if request.method == 'POST':
        email = request.POST.get('email', '')
        user = User.objects.get(id=email)
        print(user.email)
        password = request.POST.get('password', '')

        if email and password:
            if user.profile.role == 'Utilisateur':
                context = {'etablissement': Etablissement.objects.filter(code=user.profile.code_etablissement).first()}
                user = authenticate(request, email=user.email, password=password, context=context)
                return redirect('/')
            if user is not None:
                auth_login(request, user)
                
                return redirect('/')
    context = {'filter': FilterUserForm()}
    return render(request, 'account/login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('account:login')
    
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