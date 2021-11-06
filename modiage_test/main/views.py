from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import SignupForm, LoginForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html', context={'request': request})

    def post(self, request, *args, **kwargs):
        pass


class SignupView(View):
    def get(self, request, *args, **kwargs):
        form = SignupForm()
        context = {'form': form}
        return render(request, 'signup.html', context=context)

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        print(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']

            if request.POST['level'] == 'admin':
                user = User.objects.create_superuser(username, email, password)
            else:
                user = User.objects.create_user(username, email, password)

            if request.POST['level'] == 'staff':
                user.is_staff = True

            user.set_password(password)
            user.save()
            return redirect('login')

        else:
            messages.error(request, 'form is not valid')
            return redirect('signup')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context=context)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


# @login_required
class PermissionsView(View):

    def get(self, request):
        user = request.user
        if user.is_superuser:
            return render(request, 'permissions.html', context={'request': request})
        else:
            return HttpResponse('<h1>You are not valid to this stage!!!</h1>')
