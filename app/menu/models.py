from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(models.Model):
    """Menu position"""
    name = models.CharField(verbose_name='Имя', max_length=255)
    restricted = models.BooleanField(verbose_name='Только для зарегистрированных', default=False)
    published = models.BooleanField(verbose_name='Опубликовано', default=True)

    def __str__(self):
        return self.name

    def get_items(self):
        return self.menuitem_set.all()

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

class MenuItem(MPTTModel):
    """Elements of the menu"""
    name = models.CharField(verbose_name='Название пункта меню', max_length=255)
    slug = models.SlugField(verbose_name='Урл', null=True, blank=True)
    restricted = models.BooleanField(verbose_name='Только для зарегистрированных', default=False)
    sort = models.PositiveIntegerField(verbose_name='Порядок', default=0)
    published = models.BooleanField(verbose_name='Опубликовано', default=True)


    menu = models.ForeignKey(to='Menu', verbose_name='Меню', on_delete=models.CASCADE, related_name='items')
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительский пункт',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def get_absolute_url(self):
        if self.parent:
            return reverse('category', kwargs={'category_slug': self.slug})
        else:
            return reverse('page', kwargs={'page_slug': self.slug})


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


