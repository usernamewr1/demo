from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .forms import RegUser, LogUser, NewPost
from .models import Postes


# Create your views here.
def reg_user(request):
    if request.method == 'POST':
        form = RegUser(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'demo/login.html')
    else:
        form = RegUser()
    return render(request, 'demo/reg.html', {'form': form})
def log_user(request):
    if request.method == 'POST':
        form = LogUser(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
            return redirect('newpost')
    else:
        form = LogUser()
    return render(request, 'demo/login.html', {'form': form})
def logout_user(request):
    logout(request)
    return redirect('login')
def new_post(request):
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'demo/index.html')
    else:
        form = NewPost()
    return render(request, 'demo/newpost.html', {'form': form})
class PostDetail(DetailView):
    model = Postes
    template_name = 'demo/detail.html'
    context_object_name = 'post'
