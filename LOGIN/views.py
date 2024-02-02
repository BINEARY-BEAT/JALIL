from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignupForm ,UserForm
from .models import User
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

def user_login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            users = User.objects.filter(username=username)

            if not users.exists():
                form.add_error('username', 'User does not exist')
            else:
                for user in users:
                    if check_password(password, user.password):
                        # Redirect to the 'portfolio' view upon successful login
                        return redirect('fuck')

                # If no user with correct password is found
                form.add_error('password', 'Invalid password')

    else:
        form = UserForm()

    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username__iexact=username).exists():
                form.add_error('username', 'User already exists')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Account created successfully. You can now log in.')
                return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

# @login_required
def fuck(request):
    return render(request, 'fuck.html')


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer