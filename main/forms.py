from .models import Task
from django.forms import ModelForm, TextInput, Textarea, FileInput, FileField
from .models import Posts, Post
from django import forms


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        #fields = ['title', 'des', 'cover']
        fields = ("title", "des", "cover")
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "des": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),

        }

#class="btn btn-success"
#<img src="{{ post.cover.url}}" alt="{{ post.title }}", height="500px", width="500px">


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("title", "task")
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })

        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("author", "text")
        widgets = {
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш отзыв'
            }),

        }