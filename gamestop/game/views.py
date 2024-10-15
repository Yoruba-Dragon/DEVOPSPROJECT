from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse




from .models import Resturant, Store
from .forms import ResturantForm, StoreForm, SignUpForm, PasswordChangingForm



# signup page
def user_signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created' )
            return redirect('login')
    
    return render(request, 'auth/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page, e.g., home page
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangingForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully changed!')
            return redirect('game_index')
    else:
        form = PasswordChangingForm(request.user)
    return render(request, 'auth/password_change.html', {'form': form})





def game_index(request):
    """doc-string for game index function"""
    if 'f' in request.GET:
        f = request.GET['f']
        games = Resturant.objects.filter(title__icontains=f)
    else:
        games = Resturant.objects.all()
    context = {'games': games}
    return render(request, 'games/home.html', context)

def resturant_list(request):
    games = Resturant.objects.all()
    context = {'games': games}
    return render(request, 'games/resturant_list.html', context)

def store_list(request):
    games = Store.objects.all()
    context = {'games': games}
    return render(request, 'games/stores_list.html', context)



