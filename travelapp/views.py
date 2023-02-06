from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from .models import Post
from .forms import NewPostForm

def index(req):
    posts = Post.objects.all()
    return render(req, 'travelapp/index.html', {'posts': posts})

def showpost(req, id):
    post = get_object_or_404(Post, pk=id)
    return render(req, 'travelapp/showpost.html', {'post': post})

def newpost(req):
    if req.method == 'POST':
        form = NewPostForm(req.POST)

        if form.is_valid():
            post = form.save(commit=False)
            if req.user.is_authenticated:
                post.author = req.user

            post.save()

            return redirect('showpost', id=post.id)

    else:
        form = NewPostForm()

    return render(req, 'travelapp/newpost.html', {'form': form})

def user_register(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)

        if form.is_valid():
            form.save()

            return redirect('user_login')
    else:
        form = UserCreationForm()

    return render(req, 'travelapp/register.html', {'form': form})

def user_login(req):
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)

        if form.is_valid():
            login(req, form.get_user())
            return redirect('/')
    
    else:
        form = AuthenticationForm()

    return render(req, 'travelapp/login.html', {'form': form})

def user_logout(req):
    logout(req)
    return redirect('/')

def user_profile(req, username):
    if not req.user.is_authenticated:
        return redirect('user_login')

    user_posts = Post.objects.filter(author = req.user)
    return render(req, 'travelapp/user_profile.html', {'posts': user_posts})
