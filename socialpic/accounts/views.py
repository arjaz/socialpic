from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = get_user_model().objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken.'})
            except get_user_model().DoesNotExist:
                user = get_user_model().objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match.'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    #  TODO: route to index and logout
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
