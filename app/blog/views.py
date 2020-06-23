from datetime import datetime

from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import F, Q
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin, FormView
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.views.generic.base import View

from .models import Category, Tag, Post, Comment
from .forms import CommentForm


class PostDetail(DetailView, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'blog/post_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context

    def form_valid(self, form):
        form.save(commit=False)
        post = get_object_or_404(Post, slug=self.kwargs['post_slug'])
        form.instance.author = self.request.user
        form.instance.post = post
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = get_object_or_404(Post, slug=self.kwargs['post_slug'])
        return post.get_absolute_url()


class Posts(ListView):
    """Listing all categories with all posts"""
    model = Post
    template_name = 'blog/posts_all.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(published=True).select_related('category').prefetch_related('tags')


class PostsByCategory(ListView):
    """Listing posts bound to categories"""
    model = Post
    template_name = 'blog/posts_by_category.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category').prefetch_related('tags')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['category_slug'])
        print(context)
        return context


class PostsByTag(ListView):
    """Listing posts bound to tags"""
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['tag_slug']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Tag.objects.get(slug=self.kwargs['tag_slug'])
        # context['title'] = 'Записи по тегу: ' + str(Tag.objects.get(slug=self.kwargs['tag_slug']))
        return context


class Search(ListView):
    """Search for blog posts and pages"""
    paginate_by = 5
    template_name = 'blog/search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        q = self.request.GET.get('s')
        return Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q) | Q(intro_text__icontains=q))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context












