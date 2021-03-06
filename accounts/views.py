from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from accounts.forms import RegistrationForm

def signup_view(request):
    if request.method == 'POST':
         form = RegistrationForm(request.POST)
         if form.is_valid():
             user = form.save()             
             login(request, user,backend='django.contrib.auth.backends.ModelBackend')
             return redirect('articles:list')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user, 'django.contrib.auth.backends.ModelBackend')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('articles:list')