from django.db import models
from django.urls import reverse


class Page(models.Model):
    """Model for blog posts"""
    seo_title = models.CharField(verbose_name='Тег title', max_length=120)
    seo_description = models.CharField(verbose_name='Тег description', max_length=120)
    title = models.CharField(verbose_name='Заголовок', max_length=350)
    menu_title = models.CharField(verbose_name='Заголовок в меню', max_length=120)
    slug = models.SlugField(verbose_name='Урл', unique=True)
    content = models.TextField(blank=True, verbose_name='Содержимое')
    created_at = models.DateField(verbose_name='Дата публикации', auto_now_add=True)
    published = models.BooleanField(verbose_name='Опубликовано', default=True)


    def get_absolute_url(self):
        return reverse('page', kwargs={'page_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        unique_together = ('slug',)


class Feedback(models.Model):
    """Model for getting orders from contacts page"""
    name = models.CharField(verbose_name='Имя', max_length=120)
    email = models.EmailField(verbose_name="Электронная почта", max_length=300)
    subject = models.CharField(verbose_name='Тема', max_length=120)
    content = models.TextField(verbose_name='Содержимое', max_length=1400)

    def __str__(self):
        return f"{self.subject} от {self.name}"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

