from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Model to filter and render posts by category"""
    seo_title = models.CharField(verbose_name='Тег title', max_length=120)
    seo_description = models.TextField(verbose_name='Тег description', max_length=500)
    title = models.CharField(verbose_name='Заголовок', max_length=120)
    menu_title = models.CharField(verbose_name='Заголовок в меню', max_length=120)
    slug = models.SlugField(verbose_name='Урл', unique=True)
    description = models.TextField(verbose_name='Описание', max_length=1000, default='', blank=True)
    published = models.BooleanField(verbose_name='Опубликовано', default=True)


    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.menu_title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    """Model to filter and render posts by tag"""
    seo_title = models.CharField(verbose_name='Тег title', max_length=120)
    seo_description = models.TextField(verbose_name='Тег description', max_length=500)
    title = models.CharField(verbose_name='Заголовок', max_length=120)
    menu_title = models.CharField(verbose_name='Заголовок в меню', max_length=120)
    description = models.TextField(verbose_name='Описание', max_length=1000, default='', blank=True)
    slug = models.SlugField(verbose_name='Урл', unique=True)
    published = models.BooleanField(verbose_name='Опубликовано', default=True)

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    def __str__(self):
        return self.menu_title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Post(models.Model):
    """Model for blog posts"""
    seo_title = models.CharField(verbose_name='Тег title', max_length=120)
    seo_description = models.TextField(verbose_name='Тег description', max_length=500)
    title = models.CharField(verbose_name='Заголовок', max_length=350)
    slug = models.SlugField(verbose_name='Урл', unique=True)
    intro_text = models.TextField(verbose_name='Анонс')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    created_at = models.DateField(verbose_name='Дата публикации', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата обновления', auto_now=True)
    published = models.BooleanField(verbose_name='Опубликовано', default=True)
    image = models.ImageField(verbose_name='Фото', upload_to='post/', null=True, blank=True)
    views = models.PositiveIntegerField(verbose_name='Просмотры', default=0)
    featured = models.BooleanField(verbose_name='Избранная в ТОП', default=False, null=True, blank=True)

    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(to=Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(to=Tag, verbose_name='Тег', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('post', kwargs={'category_slug': self.category.slug, 'post_slug': self.slug})


    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Comment(models.Model):
    """Model for user commentaries related to blog posts"""
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Текст', max_length=1000)
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    moderated = models.BooleanField(verbose_name='Отмодерирован', default=False)

    post = models.ForeignKey(to=Post, verbose_name='Статья', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']




