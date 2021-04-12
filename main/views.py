from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .forms import PostsForm
from .forms import PostForm
from django.views.generic import ListView
from .models import Posts, Post, About
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


class PostWeb(ListView):
    model = Posts
    template_name = 'main/test1.html'


class CreatePostView(CreateView):
    model = Posts
    form_class = PostsForm
    template_name = 'main/about.html'
    success_url = reverse_lazy('main')


def index(request):
    image = Task.objects.order_by
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Cтраница сайта', 'tasks': tasks, 'images': image})


def news(request):
    news = Posts.objects.order_by('-id')
    return render(request, 'main/test1.html',  context={'news': news})


def bio(request):
    abt = About.objects.order_by('-id')
    return render(request, 'main/bio.html',  context={'abt': abt})

#'images': image


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('com')
        else:
            error = 'Форма была заполнена неверно'

    form = TaskForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def comment(request):
    com = Post.objects.order_by('-id')
    return render(request, "main/test.html", context={'cnt': com})
#inplace order_by can be all()


def t1(request):
    return render(request, 'main/test.html')
#test1


def sc(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('com')
        else:
            error = 'Форма была заполнена неверно'

    form = PostForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/otziv.html', context)


def main(request):
    return render(request, 'main/main.html')


def inf(request):
    return render(request, 'main/otziv1.html')


def prev(request):
    return render(request, 'main/prev.html')


def lastn(request):
    news = Posts.objects.order_by('-id')
    return render(request, 'main/lastn.html', context={'news': news})


def com(request):
    com = Post.objects.order_by('-id')
    return render(request, "main/com.html", context={'cnt': com})