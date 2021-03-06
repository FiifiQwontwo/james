from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import User


@csrf_protect
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('Attendance:home page')

        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return render(request, "login.html", {})
    return render(request, "login.html", {})



def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logout ')
    return redirect('Attendance:home page')


# @login_required(login_url='accounts:user_login')
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have Signup'))
            return redirect('Attendance:home page')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def edit_user(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.success(request, 'You have Updated Your Profile')
            return redirect('Attendance:home page')
    else:
        form = EditUserForm(instance=request.user)
    context = {'form': form}
    return render(request, 'update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You have Updated Your Password')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'passewordchange.html', context)
