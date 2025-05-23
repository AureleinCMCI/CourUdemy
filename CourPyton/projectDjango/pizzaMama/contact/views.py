from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, SignInForm

def signup_login_view(request):
    signup_form = SignUpForm()
    signin_form = SignInForm()
    
    is_signup = False
    if request.method == 'POST':
        if 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            show_signup = True  # Affiche le formulaire d'inscription
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('home')  # Redirige après inscription réussie
        elif 'signin' in request.POST:
            signin_form = SignInForm(request, data=request.POST)
            if signin_form.is_valid():
                user = authenticate(
                    username=signin_form.cleaned_data['username'],
                    password=signin_form.cleaned_data['password']
                )
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Redirige après connexion réussie

    return render(request, 'contact/signup_login.html', {
        'signup_form': signup_form,
        'signin_form': signin_form,
        'is_signup': is_signup,  # ✔️ on l'envoie au template

    })
