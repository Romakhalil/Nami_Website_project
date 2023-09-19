from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log in the user
            login(request, form.get_user())
            return redirect('dashboard')  # Redirect to the dashboard or another page after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user after successful signup
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard or another page after signup
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout
