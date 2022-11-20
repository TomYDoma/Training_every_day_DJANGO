# blog/views.py
import datetime

from django.views.generic import ListView, DetailView  # новое
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView): # Создание нового класса
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')

