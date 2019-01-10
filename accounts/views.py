from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from accounts.forms import Account_Form
from accounts.models import Account

def profile(request, pk):
    acc = get_object_or_404(Account, pk=pk)
    
    return render(request, "accounts/profile.html", {
            'instance': acc,
            'image': acc.avatar
            })


def login_view(request):
    success_url = reverse_lazy('main:main')
    if request.method == 'POST':
        usr = request.POST.get('username')
        psw = request.POST.get('password')
        user = authenticate(username=usr, password=psw)

        if user and user.is_active:
            login(request, user)
            return redirect(success_url)

    return render(request, 'accounts/login.html')


def logout_view(request):
    success_url = reverse_lazy('main:main')
    logout(request)
    return redirect(success_url)


def registration(request):
    template_name = "accounts/registration.html"
    success_url = reverse_lazy('accounts:login')
    form = Account_Form(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form})


def account_update(request, pk):
    template_name = "accounts/registration.html"
    success_url = reverse_lazy('accounts:login')
    acc = get_object_or_404(Account, pk=pk)
    form = Account_Form(instance=acc)

    if request.method == 'POST':
        form = Account_Form(
            request.POST,
            instance=acc
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form})
